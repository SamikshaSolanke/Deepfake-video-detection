from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import numpy as np
from utils.video_processing import frames_extract, frame_preprocess
import tensorflow as tf

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load TFLite model
TFLITE_MODEL_PATH = './model/deepfake_detector_model4.tflite'
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_deepfake(video_path):
    frames = frames_extract(video_path)
    predictions = []

    for frame in frames:
        processed_frame = frame_preprocess(frame)
        processed_frame = np.expand_dims(processed_frame, axis=0).astype(np.float32)

        if processed_frame.shape != tuple(input_details[0]['shape']):
            raise ValueError(f"Input shape mismatch. Expected: {tuple(input_details[0]['shape'])}, Got: {processed_frame.shape}")

        interpreter.set_tensor(input_details[0]['index'], processed_frame)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]
        predictions.append(prediction)

    avg_prediction = np.mean(predictions)
    confidence = avg_prediction * 100
    return confidence


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['video']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            confidence = predict_deepfake(file_path)
            os.remove(file_path)
            return jsonify({'deepfake_percentage': f'{confidence:.2f}%'})
        except Exception as e:
            os.remove(file_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format. Only .mp4 is allowed.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
