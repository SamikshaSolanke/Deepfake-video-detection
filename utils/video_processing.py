# import cv2
# import numpy as np
#
# def frames_extract(video_path, max_frames=10, frame_size=(224, 224)):
#     cap = cv2.VideoCapture(video_path)
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     total_frames = int(min(cap.get(cv2.CAP_PROP_FRAME_COUNT), fps * 10))
#     frame_interval = max(total_frames // max_frames, 1)
#     frames = []
#     count = 0
#
#     while len(frames) < max_frames:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         if count % frame_interval == 0:
#             resized_frame = cv2.resize(frame, frame_size)
#             frames.append(resized_frame)
#         count += 1
#
#     cap.release()
#     return frames
#
# def frame_preprocess(frame):
#     return frame / 255.0

import cv2
import numpy as np

def frames_extract(video_path, max_frames=10, frame_size=(224, 224), face_cascade_path="haarcascade_frontalface_default.xml"):

    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(min(cap.get(cv2.CAP_PROP_FRAME_COUNT), fps * 10))  # Limit to 10 seconds
    frame_interval = max(total_frames // max_frames, 1)
    frames = []
    count = 0

    while len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Process only frames at the specified interval
        if count % frame_interval == 0:
            # Convert frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # If faces are detected, crop the first detected face
            if len(faces) > 0:
                x, y, w, h = faces[0]  # Use the first detected face
                face_frame = frame[y:y+h, x:x+w]

                # Resize the face frame to the specified size
                resized_frame = cv2.resize(face_frame, frame_size)
                frames.append(resized_frame)
            else:
                print(f"No face detected in frame {count}. Skipping.")
        count += 1

    cap.release()
    return frames

def frame_preprocess(frame):
    return frame / 255.0  # Normalize pixel values to [0, 1]

# Example usage
if __name__ == "__main__":
    video_path = "path_to_your_video.mp4"
    extracted_frames = frames_extract(video_path)
    print(f"Extracted {len(extracted_frames)} frames with detected faces.")

