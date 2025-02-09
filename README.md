# 📌 Smart Vision System

## 📝 **Project Description**
The **Smart Vision System** is an AI-powered assistive technology designed to help visually impaired individuals perceive their surroundings.
The system integrates **image processing, object detection, speech recognition, and text-to-speech conversion** to provide real-time audio feedback about detected objects and their distances.

## 🚀 **Features**
- 🖼️ **Object Detection**: Uses **SSD MobileNet** to detect and classify objects in the environment.
- 🔢 **Distance Calculation**: Estimates the distance between detected objects.
- 🎤 **Voice Commands**: Supports voice input using **Speech Recognition**.
- 🔊 **Audio Feedback**: Converts detected objects into speech using **pyttsx3**.
- 📷 **Real-time Processing**: Captures and processes live video frames from a camera.

## 🏗️ **Project Structure**
```
Smart-Vision-System/
│── models/                     # Folder for AI models
│   ├── ssd_mobilenet.tflite     # If using TFLite
│   ├── ssd_mobilenet.pb         # If using TensorFlow
│
│── src/                         # Source code files
│   ├── main.py                  # Main entry point
│   ├── ai_integration.py        # Handles AI model processing
│   ├── image_processing.py      # Processes images for object detection
│   ├── speech_recognition.py    # Voice input handling
│
│── config/                      # Configuration files
│   ├── config.json              # Stores settings
│
│── docs/                        # Documentation folder
│   ├── README.md                # Main project documentation
│
│── requirements.txt             # Python dependencies
│── .gitignore                   # Ignore unnecessary files
│── LICENSE                      # License file
```

## 🔧 **Installation & Setup**
### **1️⃣ Prerequisites**
Ensure you have **Python 3.8+** installed on your system.

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/Smart-Vision-System.git
cd Smart-Vision-System
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```sh
python src/main.py
```

## 📦 **Dependencies (requirements.txt)**
```txt
openai
opencv-python
numpy
tensorflow
pyttsx3
SpeechRecognition
```

## 🎯 **How It Works**
1. **Captures** real-time video using OpenCV.
2. **Processes** frames using **SSD MobileNet** to detect objects.
3. **Recognizes** user voice commands for interaction.
4. **Converts** detected objects into speech output using pyttsx3.

## 📷 **Demo Screenshot**
![Demo](https://your-image-url.com/demo.png)  

## 🛠️ **Technologies Used**
- **Python** (Programming Language)
- **OpenCV** (Computer Vision)
- **TensorFlow SSD MobileNet** (AI Model for Object Detection)
- **SpeechRecognition** (Voice Input Handling)
- **pyttsx3** (Text-to-Speech Conversion)

🤝 **Contributing**
1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

📝 **License**
This project is licensed under the MIT License.

📬 **Contact**
📧 Email: bharani232427@gmail.com  
🐙 GitHub: https://github.com/bharani-coder-27
🚀 LinkedIn: www.linkedin.com/in/bharanidharan27 

