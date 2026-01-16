# A.Eye - Artificial Eye

**An AI-Powered Assistive Device for the Blind and Visually Impaired**

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Implementation](#technical-implementation)
- [Performance Metrics](#performance-metrics)
- [Project Team](#project-team)
- [Acknowledgments](#acknowledgments)
- [Future Work](#future-work)
- [License](#license)

---

## Overview

**A.Eye (Artificial Eye)** is a graduation project from Menoufia University's Faculty of Electronic Engineering, developed in 2021/2022. This standalone assistive device leverages artificial intelligence, computer vision, and image processing to help blind and visually impaired individuals navigate their daily lives with greater independence.

The device combines a Raspberry Pi 4 Model B with a camera module and advanced AI algorithms to provide real-time object detection, face recognition, currency identification, and text reading capabilities—all through voice interaction.

### Key Highlights

- **Standalone Operation**: Works independently without requiring internet connectivity
- **Real-time Processing**: Provides instant feedback through voice output
- **Affordable Solution**: Designed to be cost-effective for the MENA region (under 5,000 EGP)
- **Wearable Design**: 3D-printed wristwatch form factor for convenience
- **Voice-Activated**: Hands-free operation through voice commands

---

## Problem Statement

### Vision Impairment Statistics

- **Globally**: 2.2 billion people have near or distant vision impairment, with 1 billion having severe impairment or blindness
- **In Egypt**: 3 million visually impaired individuals and 1 million blind people
- **Prosopagnosia (Face Blindness)**: Affects approximately 2% of the population
- **Dyslexia (Reading Disorder)**: Affects 5-10% of the worldwide population

### Our Solution

A.Eye addresses these challenges by providing:
- Real-time object and obstacle detection
- Face recognition for acquaintances and family members
- Text reading capabilities for written materials
- Currency identification for financial independence

---

## Features

### Core Capabilities

#### 1. Object Detection
- **Algorithm**: YOLOv4 (You Only Look Once)
- **Detection Speed**: 15-30 FPS
- **Objects Recognized**: 80 different object classes
- **Distance Calculation**: Estimates object distance from camera using triangle similarity
- **Voice Feedback**: Announces detected objects and their approximate distance

#### 2. Face Recognition
- **Technology**: Deep learning with 128-dimensional face embeddings
- **Accuracy**: Approximately 95%
- **Process**:
  - HOG (Histogram of Oriented Gradients) for face detection
  - 68 facial landmarks identification
  - Face encoding using pre-trained neural networks
  - SVM classifier for person identification
- **Real-time Recognition**: Continuously identifies known individuals

#### 3. Money Recognition
- **Currency**: Egyptian Pound (EGP)
- **Denominations**: All current Egyptian currency notes
- **Custom Training**: Trained on custom-collected dataset of Egyptian currency
- **Technology**: YOLOv4 with custom weights
- **Application**: Helps users identify currency independently

#### 4. Text Recognition (OCR)
- **Engine**: Tesseract OCR
- **Accuracy**: Approximately 90% on clear text
- **Preprocessing Pipeline**:
  - RGB to Grayscale conversion
  - Image resizing (1.5x for optimal DPI)
  - CLAHE (Contrast Limited Adaptive Histogram Equalization)
  - Otsu's binarization
  - Skew correction using projection profile method
  - Median filter noise removal
- **Supported Text**: Printed materials, signs, labels, documents

#### 5. Voice Recognition
- **Engine**: Vosk (offline speech recognition)
- **Recognition Engine**: Kaldi ASR
- **Response Time**: Near real-time
- **Commands**: Activate different modes (object detection, face recognition, text reading, money recognition)

#### 6. Text-to-Speech
- **Output**: High-quality audio feedback
- **Interface**: 3.5mm audio jack via USB sound card
- **Feedback Type**: Descriptive voice output for all detected information

---

## Hardware Components

### Main Apparatus

| Component | Specification | Price (EGP) |
|-----------|--------------|-------------|
| **Raspberry Pi 4 Model B** | 8GB RAM, 1.5GHz 64-bit quad-core CPU | 1,880 |
| **Raspberry Pi Camera V2** | 8MP, Sony IMX219 sensor | 800 |
| **Power Bank** | Xiaomi 10,000mAh | 400 |
| **USB Sound Card** | External audio interface | 20 |
| **Earphone Splitter** | Audio input/output | 15 |
| **3D Printed Case** | Wristwatch form factor | 400 |
| **MicroSD Card** | 32GB Samsung EVO+ Class 10 | Included in kit |
| **Heat Sinks** | Thermal management | Included in kit |
| **Total Cost** | | **3,515 EGP** |
**Note that these prices are according to 2022. They may vary in the future.**

### Included Accessories
- Raspberry Pi Case with integrated fan
- USB-C Power Supply (3.5A)
- Micro HDMI to HDMI Cable
- USB MicroSD Card Reader
- Set of heat sinks

### Form Factor

The device is designed as a **wristwatch** with:
- 3D-printed case housing the Raspberry Pi
- Camera module positioned in a slider above the cover
- Earphones connected under the user's shirt
- Point-and-capture functionality by directing the watch

---

## Technology Stack

### Programming & Frameworks
- **Python 3.x** - Primary programming language
- **OpenCV** - Computer vision and image processing
- **TensorFlow** - Deep learning framework support

### AI & Machine Learning
- **YOLOv4** - Object and currency detection
- **Face Recognition Library** (by Adam Geitgey)
- **OpenFace** - Face encoding
- **dlib** - Machine learning algorithms
- **Tesseract OCR** - Text recognition

### Voice Processing
- **Vosk** - Offline speech recognition
- **Kaldi** - ASR engine
- **pyttsx3/gTTS** - Text-to-speech synthesis

### Core Libraries
- **NumPy** - Numerical computing
- **PIL/Pillow** - Image manipulation
- **SciPy** - Scientific computing

### Operating System
- **Raspbian OS (Raspberry Pi OS)** - Debian-based Linux distribution

---

## Installation

### Prerequisites

- Raspberry Pi 4 Model B (4GB+ RAM recommended)
- Raspberry Pi Camera Module V2
- MicroSD card (32GB+, Class 10)
- USB sound card
- Earphones with microphone
- Power bank or 5V 3A USB-C power supply

### Step 1: Prepare the MicroSD Card

1. **Download NOOBS**
   ```
   Visit: https://www.raspberrypi.org/downloads/
   Download: NOOBS Offline and network install
   ```

2. **Format the MicroSD Card**
   - Use SD Card Formatter tool from https://www.sdcard.org/
   - Format as FAT32
   - Label as "NOOBS"

3. **Install NOOBS**
   - Extract NOOBS archive
   - Copy all files to the MicroSD card
   - Safely eject the card

### Step 2: Initial Raspberry Pi Setup

1. **Insert the MicroSD card** into Raspberry Pi
2. **Connect peripherals**:
   - HDMI cable to monitor
   - USB keyboard and mouse
   - Network cable (optional)
3. **Power on** and follow the Welcome Wizard
4. **Install Raspbian Full** from NOOBS menu

### Step 3: Enable Required Interfaces

```bash
# Open Raspberry Pi Configuration
sudo raspi-config
```

Enable the following in "Interface Options":
- Camera
- SSH
- VNC (optional, for remote access)

Reboot after changes:
```bash
sudo reboot
```

### Step 4: Clone the Repository

```bash
cd ~/Desktop
git clone https://github.com/ahmedelbrawany/A.Eye.git
cd A.Eye
```

### Step 5: Install Python Dependencies

```bash
# Update system packages
sudo apt-get update
sudo apt-get upgrade -y

# Install Python 3 and pip
sudo apt-get install python3-pip -y

# Install OpenCV
sudo apt-get install python3-opencv -y

# Install required Python packages
pip3 install numpy
pip3 install pillow
pip3 install vosk
pip3 install face-recognition
pip3 install pytesseract
pip3 install pyttsx3

# Install Tesseract OCR
sudo apt-get install tesseract-ocr -y
```

### Step 6: Install YOLO Dependencies

```bash
# Install darknet (for YOLO)
# Follow the instructions in the Money_Recognition and Object_Recognition directories
```

### Step 7: Configure Auto-Start on Boot

1. **Create launcher script**:
   ```bash
   cd ~/Desktop/A.Eye/Main
   nano launcher.sh
   ```

2. **Add the following content**:
   ```bash
   #!/bin/sh
   # launcher.sh
   cd /
   cd home/pi/Desktop/A.Eye/Main
   sudo python3 Main.py
   cd /
   ```

3. **Make it executable**:
   ```bash
   chmod 755 launcher.sh
   ```

4. **Add to crontab**:
   ```bash
   sudo crontab -e
   ```
   
   Add this line at the end:
   ```
   @reboot sh /home/pi/Desktop/A.Eye/Main/launcher.sh >/home/pi/logs/cronlog 2>&1
   ```

5. **Create logs directory**:
   ```bash
   mkdir ~/logs
   ```

### Step 8: Connect Hardware

1. **Camera Module**:
   - Power off Raspberry Pi
   - Connect ribbon cable to CSI port
   - Ensure proper orientation (blue side up)

2. **USB Sound Card**:
   - Connect to USB port
   - Connect earphone splitter
   - Connect earphones

3. **Test the setup**:
   ```bash
   raspistill -o test.jpg
   ```

---

## Usage

### Voice Commands

A.Eye responds to the following voice commands:

| Command | Function |
|---------|----------|
| **"Recognize face"** | Activates face recognition mode |
| **"What's this?"** | Identifies objects in camera view |
| **"Read text"** | Extracts and reads text from images |
| **"Check money"** | Identifies currency denomination |
| **"Exit"** or **"Stop"** | Closes the current mode |

### Operating Modes

#### 1. Object Detection Mode
- Point the watch towards objects
- System announces detected objects and approximate distance
- Helps identify obstacles and navigate environment

#### 2. Face Recognition Mode
- Add known faces to the database first
- Point towards people
- System announces recognized person's name
- Unknown faces are noted as "Unknown"

#### 3. Text Reading Mode
- Point camera at text (signs, labels, documents)
- System reads aloud the detected text
- Works best with clear, well-lit text

#### 4. Money Recognition Mode
- Point camera at Egyptian currency
- System announces the denomination
- Helps in financial transactions

### Adding New Faces

1. Navigate to the Face_Recognition directory
2. Create a folder with the person's name
3. Add 15-20 clear photos of the person's face
4. Run the training script
5. The person will now be recognized

---

## Technical Implementation

### Object Detection (YOLOv4)

**How it Works**:
1. **Grid Division**: Image divided into SxS grid cells
2. **Bounding Box Regression**: Each cell predicts bounding boxes with confidence scores
3. **IOU Calculation**: Intersection over Union determines overlapping boxes
4. **Non-Maximum Suppression**: Removes duplicate detections
5. **Distance Estimation**: Uses triangle similarity with known object widths

**Formula for Distance Calculation**:
```
F = (P × D) / W    (Focal Length)
D = (W × F) / P    (Distance)

Where:
- P = Apparent width in pixels
- D = Distance from camera
- W = Actual width of object
- F = Focal length of camera
```

### Face Recognition Pipeline

**4-Step Process**:

1. **Face Detection (HOG)**
   - Convert image to grayscale
   - Calculate gradients for each pixel
   - Group into 16x16 pixel squares
   - Find patterns matching known face structures

2. **Face Alignment**
   - Detect 68 facial landmarks
   - Apply affine transformations
   - Center eyes and mouth
   - Normalize face orientation

3. **Face Encoding**
   - Deep CNN generates 128 measurements
   - Creates unique "face fingerprint"
   - Uses triplet training methodology
   - Pre-trained OpenFace network

4. **Face Matching**
   - Linear SVM classifier
   - Compares encodings with database
   - Returns closest match
   - Approximately 95% accuracy

### Money Recognition

**Custom Training Process**:
1. Data collection of Egyptian currency
2. Image labeling using LabelImg
3. YOLOv4 model training with custom weights
4. Model optimization for Raspberry Pi
5. Real-time detection implementation

### Text Recognition (Tesseract)

**Preprocessing Pipeline**:
1. **RGB to Grayscale**: Reduce processing complexity
2. **Resizing**: Scale to 300-600 DPI for optimal OCR
3. **CLAHE**: Enhance contrast in local regions
4. **Binarization**: Convert to black and white using Otsu's method
5. **Skew Correction**: Align text horizontally
6. **Noise Removal**: Apply median filter

**OCR Process**:
1. Connected component analysis
2. Line finding and baseline fitting
3. Word segmentation
4. Character classification
5. Text output

### Voice Recognition (Vosk + Kaldi)

**Processing Steps**:
1. **Audio Sampling**: 16KHz sampling rate
2. **Preprocessing**: 20ms audio chunks
3. **Fourier Transform**: Break into frequency components
4. **Spectrogram Generation**: Create visual representation
5. **RNN Recognition**: Recurrent Neural Network predicts characters
6. **Text Cleanup**: Remove duplicates and blanks
7. **Language Model**: Select most likely transcription

---

## Performance Metrics

### Accuracy Metrics

| Feature | Accuracy | Speed |
|---------|----------|-------|
| **Face Recognition** | ~95% | Real-time |
| **Object Detection** | High (YOLO) | 15-30 FPS |
| **Text Recognition** | ~90% (clear text) | Variable |
| **Voice Recognition** | ~85% | Near real-time |
| **Money Recognition** | High | Variable |

### System Performance

- **Response Time**: Less than 1 second for standard operations
- **Danger Alerts**: Less than 200ms
- **Battery Life**: Full day with 10,000mAh power bank
- **System Uptime**: Near-zero failure rate
- **Processing**: Raspberry Pi 4 quad-core 1.5GHz

### Success Measurements

- Single charge per day battery life
- High-performance with minimal downtime
- Sub-second response for typical use cases
- Cost under 5,000 EGP for Egyptian market
- Target: 70%+ user satisfaction rating

---

## Project Team

**Supervisor**: Assoc. Prof. Marwa A. Shouman

**Team Members**:
- [**Ahmed Mohamed Abouzid El-Brawany**](https://www.linkedin.com/in/ahmed-elbrawany) - Lead Software Engineer
- [**AbdElaziz Ahmed Elsayed Elahwal**](https://www.linkedin.com/in/abdelaziz-ahmed-a954951bb) - Hardware Engineer
- [**Ahmad Tharwat Mustafa Abd El-Hameed**](https://www.linkedin.com/in/ahmad-tharwat) - Operations Engineer

**Institution**: Menoufia University, Faculty of Electronic Engineering  
**Department**: Computer Science and Engineering  
**Academic Year**: 2021/2022

---

## Acknowledgments

Special thanks to:

- **Prof. Marwa Shouman** - Project supervisor for guidance and support
- **Eng. Murtaza Hassan** - Founder of Murtaza Workshop YouTube channel for tutorials
- **Eng. Adam Geitgey** - Machine Learning instructor for face recognition insights
- **Joseph Redmon & Ali Farhadi** - Original YOLO algorithm authors
- **Alexey Bochoknovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao** - YOLOv4 developers
- **Raspberry Pi Foundation** - For creating accessible computing hardware

---

## Future Work

### Planned Enhancements

- **Arabic Language Support** - Add Arabic voice recognition and TTS for regional users
- **Expanded Object Database** - Train YOLO on more objects for better coverage
- **LED Flashlight** - Improve night-time image capture quality
- **GPS Navigation** - Add navigation assistance for outdoor mobility
- **Mobile/Web Applications** - Remote monitoring and feature management
- **Model Optimization** - Improve accuracy across all AI models
- **Speed Optimization** - Faster money recognition processing
- **Multi-Currency Support** - Recognize currencies beyond EGP
- **Cloud Integration** - Optional cloud-based processing for enhanced features
- **Smart Home Integration** - Connect with IoT devices
- **Wearable Versions** - Develop smart glasses variant

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Documentation

For comprehensive technical documentation, please refer to the [Book/Book.pdf](Book/Book.pdf) which includes:
- Complete feasibility study
- Detailed hardware setup guide
- In-depth technical explanations of all algorithms
- Code appendices
- Market research and analysis
- Performance testing results

---

## Contact

**Ahmed El-Brawany**  
Project Lead & Developer  
GitHub: [@ahmedelbrawany](https://github.com/ahmedelbrawany)  
Project Repository: [A.Eye](https://github.com/ahmedelbrawany/A.Eye)

---

## References

For detailed references including research papers, tools, and libraries used, please see pages 91-93 of the project book.

Key technologies:
- [Raspberry Pi Official Documentation](https://www.raspberrypi.org/documentation/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
- [Face Recognition by Adam Geitgey](https://github.com/ageitgey/face_recognition)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Vosk Speech Recognition](https://alphacephei.com/vosk/)

---

**Made with dedication for the visually impaired community**  
*Empowering independence through artificial intelligence*

Menoufia University • Faculty of Electronic Engineering • 2021/2022
