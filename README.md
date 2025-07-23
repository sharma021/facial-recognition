# Face Recognition Attendance System

A real-time, ML-based facial recognition system for automated attendance logging, built with Python, OpenCV, and MySQL.

---

## ⭐ Overview

This project automates the process of attendance marking using computer vision. It leverages OpenCV for face detection and recognition and logs all attendance events in a MySQL database. The system reduces manual errors and enables secure, contactless attendance for classrooms or office environments.

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Libraries:** OpenCV, NumPy, MySQL Connector
- **Database:** MySQL
- **Algorithms:** Haar Cascade (face detection), LBPH (face recognition)

---

## 🚀 Features

- **Face Detection:** Uses Haar Cascade classifier for real-time face detection via webcam.
- **Face Recognition:** Employs the LBPH algorithm to recognize faces from a trained dataset.
- **Attendance Logging:** Stores recognized faces and timestamps directly in a MySQL database.
- **Contactless Attendance:** Enables secure, efficient, and paperless attendance taking.
- **Modular Structure:** Includes separate modules for data collection, training, and recognition.

---

## 📷 Demo

*Screenshots incoming*

---

## 📦 How to Run

1. **Clone this repository:**
    ```bash
    git clone https://github.com/sharma021/facial-recogniton.git
    cd facial-recogniton
    ```

2. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If requirements.txt is missing, list your main dependencies: opencv-python, numpy, mysql-connector-python)*

3. **Configure MySQL Database:**
    - Create a new database in MySQL (e.g., `attendance_db`).
    - Update your database connection details in the code (typically in `db_config.py` or wherever credentials are set).

4. **Collect Training Data:**
    - Run the data collection script to capture and store images of each person for training.
    - Example:
      ```bash
      python dataset_collector.py
      ```

5. **Train the Model:**
    - Run the training script to process the images and create the LBPH model.
    - Example:
      ```bash
      python trainer.py
      ```

6. **Start Attendance Recognition:**
    - Run the main attendance script. It will use the webcam for real-time recognition and log entries to the database.
    - Example:
      ```bash
      python main.py
      ```

---

## 🗃️ Folder Structure
facial-recogniton/
│
├── dataset_collector.py # Script to collect training images
├── trainer.py # Script to train LBPH face recognizer
├── main.py # Real-time recognition & attendance logging
├── requirements.txt # Python dependencies
├── README.md # Project overview (this file)
└── ... # Other support files
