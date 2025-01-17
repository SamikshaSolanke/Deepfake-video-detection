import cv2

def extract_frames(video_path, max_frames=20, frame_size=(224, 224)):
    """
    Extract frames from a video file.
    """
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(total_frames // max_frames, 1)
    frames = []
    count = 0

    while len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            resized_frame = cv2.resize(frame, frame_size)
            frames.append(resized_frame)
        count += 1

    cap.release()
    return frames

def preprocess_frame(frame):
    """
    Preprocess frame for the TFLite model.
    Normalize to [0, 1] range and resize if needed.
    """
    frame = frame / 255.0  # Normalize pixel values
    return frame


