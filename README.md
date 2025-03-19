# Deepfake Video Detection

## Setup Instructions

1. **Clone the GitHub repository** to your desired location:
   ```bash
   git clone https://github.com/SamikshaSolanke/Deepfake-video-detection.git
2. Go to the main folder:
   ```bash
   cd Deepfake-video-detection-main
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
5. Click on the link which appears on the terminal/ cmd
6. **To test the model, please upload the videos provided in test folder**
<br>

## Useful Links
- **GitHub Repository:** [github.com/SamikshaSolanke/Deepfake-video-detection](https://github.com/SamikshaSolanke/Deepfake-video-detection)
- **Kaggle Dataset:** [kaggle.com/datasets/reubensuju/celeb-df-v2](https://www.kaggle.com/datasets/reubensuju/celeb-df-v2)
- **Dataset we used:** [drive.google.com/drive/folders/1ZwyawT2beV9pVDZlNePAq4pcagByWPmj?usp=sharing](https://drive.google.com/drive/folders/1ZwyawT2beV9pVDZlNePAq4pcagByWPmj?usp=sharing)
- **Pre-processed data(frames):** [drive.google.com/drive/folders/1bZBl5CgnfKwoial2eoUHwYlrxdwPyPHZ?usp=sharing](https://drive.google.com/drive/folders/1bZBl5CgnfKwoial2eoUHwYlrxdwPyPHZ?usp=sharing)

<br>

## Problem Statement Description
- **Prevalence of Deepfakes:** Growing concern with widespread usage in social media and video communications.
- **Vulnerability in Mobile Platforms:** Users on WhatsApp and Skype are increasingly exposed to deepfake scams and identity theft.
- **Real-time Challenge:** The need for instantaneous detection during live video calls to prevent misinformation and fraud.
- **Technical Constraints:** Limited processing power on mobile devices requires an efficient, lightweight solution.

<br>

## Tech Stack Used
- **Python:** Core programming language for the backend, chosen for its robust libraries in machine learning and video processing.
- **TensorFlow:** Framework for training the deepfake detection model.
- **MobileNetV2:** The lightweight MobileNetV2 backbone ensures the model runs efficiently on mobile devices..
- **TensorFlow Lite:** Deployed the trained deepfake detection model in a mobile-compatible, lightweight format.
- **Flask:**used for building web app.
- **OpenCV:** Preprocessing video frames (e.g., extraction and resizing).

<br>

## Architecture
![Screenshot 2025-01-17 102557](https://github.com/user-attachments/assets/34865b0c-ca44-471d-abad-1a7b8f7f1796)

<br>

## Results
![Screenshot 2025-01-17 102818](https://github.com/user-attachments/assets/fd3d6c33-d2ae-4aba-9354-938651644cef)
