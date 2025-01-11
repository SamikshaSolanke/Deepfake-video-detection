# Deepfake Video Detection - CSI Codezilla

<br>
![Alt text](images/example.png)

## Useful Links
- **GitHub Repository:** [github.com/SamikshaSolanke/Deepfake-video-detection-CSI-Codezilla](https://github.com/SamikshaSolanke/Deepfake-video-detection-CSI-Codezilla)
- **Kaggle Dataset:** [https://www.kaggle.com/datasets/reubensuju/celeb-df-v2](https://www.kaggle.com/datasets/reubensuju/celeb-df-v2)
- **Preprocessed Dataset:** [[https://drive.google.com/drive/folders/1s_WIcftTjf1MbsadQmcM7bGeMI73yVaI?usp=drive_link](https://drive.google.com/drive/folders/12kt5EH6h1dRInoBHCcVBKiJbW0vL4vi9?usp=sharing)]([https://drive.google.com/drive/folders/1s_WIcftTjf1MbsadQmcM7bGeMI73yVaI?usp=drive_link](https://drive.google.com/drive/folders/12kt5EH6h1dRInoBHCcVBKiJbW0vL4vi9?usp=sharing))
- **CSV File:** [[https://drive.google.com/file/d/1teY_IySry9hDMChIL0Jjhi0d3cFNifKo/view?usp=drive_link]([https://drive.google.com/file/d/1-JnAA7dx_sHuhy0j5jnKpnmfBJOu3Qg1/view?usp=sharing)](https://drive.google.com/file/d/1teY_IySry9hDMChIL0Jjhi0d3cFNifKo/view?usp=drive_link](https://drive.google.com/file/d/1-JnAA7dx_sHuhy0j5jnKpnmfBJOu3Qg1/view?usp=sharing))

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
- **MobileNetV2:** The lightweight MobileNetV2 backbone ensures the model runs efficiently on mobile devices.
- **MongoDB:** For storing detection logs and metadata.
- **React Native:** Framework for building the cross-platform mobile app.
- **TensorFlow Lite:** Deployed the trained deepfake detection model in a mobile-compatible, lightweight format.
- **FastAPI:** Backend framework for creating RESTful APIs.
- **OpenCV:** Preprocessing video frames (e.g., extraction and resizing).
