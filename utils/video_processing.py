import cv2
import numpy as np

def frames_extract(video_path, max_frames=10, frame_size=(224, 224)):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(min(cap.get(cv2.CAP_PROP_FRAME_COUNT), fps * 10))
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

def frame_preprocess(frame):
    return frame / 255.0
