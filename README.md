# 🚀 Deep Learning-Based Illegal Bowling Action Detection

## Research paper

See [the paper reference](papers/README.md) for the arXiv paper, citation,
source metadata, and a command to download a verified local PDF:

```bash
python3 papers/fetch_paper.py
```

## 📌 Overview

This repository provides a deep learning-based solution for detecting illegal bowling actions in cricket using computer vision techniques. The system identifies illegal bowling actions by analyzing the arm's angle difference between two key frames in a bowler's delivery: **the shoulder frame** and **the release frame**. If the angle difference exceeds a predefined threshold (15 degrees), the action is flagged as illegal.

## 🚀 Features

✅ **Pose Estimation using MediaPipe**  
✅ **Object Detection with YOLOv8 for release frame extraction**  
✅ **Video Processing from multiple angles (front, back, and side)**  
✅ **High Accuracy: 91.96% accuracy and 100% true positive rate**  
✅ **Real-time Detection suitable for live cricket matches**  

## 📂 Dataset

📌 **62 videos featuring 11 male bowlers**  
📌 **Footage includes both legal and illegal bowling actions**  
📌 **Labeled dataset used for training and validation**  

## 📖 Methodology

### 🔹 Dataset Collection & Preprocessing
Videos are labeled based on **ICC bowling rules**.

### 🔹 Frame Extraction
📌 **Shoulder Frame Extraction**: Detects the arm closest to shoulder level (270° angle).  
📌 **Release Frame Extraction**: Uses YOLOv8 to detect when the bowler releases the ball.  

### 🔹 Bowling Action Analysis
📌 Measures **elbow flexion** using **MediaPipe**.  
📌 If the angle difference exceeds **15°**, the delivery is flagged as **illegal**.  

### 🔹 Model Evaluation
📌 Tested with accuracy, precision, recall, and F1-score.  
📌 Compared different models (**CNN, YOLOv7, YOLOv8**) for optimal performance.  

