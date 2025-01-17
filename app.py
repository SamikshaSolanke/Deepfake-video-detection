from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import cv2
from utils.video_processing import extract_frames, preprocess_frame

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load TFLite model
TFLITE_MODEL_PATH = './model/deepfake_detector_model_final.tflite'
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL_PATH)
interpreter.allocate_tensors()

# Get input/output details from the model
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def allowed_file(filename):
    """Check if the uploaded file is an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_deepfake(video_path):
    """Process the video and predict if it is deepfake."""
    frames = extract_frames(video_path, max_frames=20, frame_size=(224, 224))
    predictions = []

    for frame in frames:
        processed_frame = preprocess_frame(frame)  # Normalize frame to [0, 1]
        processed_frame = np.expand_dims(processed_frame, axis=0)  # Add batch dimension

        interpreter.set_tensor(input_details[0]['index'], processed_frame.astype(np.float32))
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]['index'])
        predictions.append(prediction[0][0])

    avg_prediction = np.mean(predictions)
    return avg_prediction


@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """Handle video uploads and deepfake detection."""
    if 'video' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['video']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Run prediction
        deepfake_score = predict_deepfake(file_path)
        percentage = deepfake_score * 100  # Convert to percentage

        # Delete the uploaded file after processing
        os.remove(file_path)

        return jsonify({'deepfake_percentage': f'{percentage:.2f}%'})
    else:
        return jsonify({'error': 'Invalid file format. Only .mp4 is allowed.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
