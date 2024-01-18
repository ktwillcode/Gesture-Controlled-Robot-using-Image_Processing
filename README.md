# **Gesture-Controlled Robot using Image Processing**

This repository contains Python code for a gesture-controlled robot that utilizes image processing techniques. The project comprises two main codes: one for **hand gesture recognition** and the other for **facial expression recognition** to control the movement of a robot car.

![Robot Car Image](/Image-robo.jpg)

## **Project Overview**

The primary goal of this project is to control a robot car using hand gestures and facial expressions captured by a camera connected to a laptop. The laptop processes the image data and communicates the movement instructions to an **Arduino Uno** via a USB long wire (serial connection).

## **Hardware Used**

- **Robot Components:**
    - Car chassis
    - Arduino Uno
    - Motor driver L293d
    - Switch
    - Battery

- **Additional Components:**
    - Laptop with a camera for image processing

## **Folder Structure**

- **`hand_gesture_control/`**: Contains Python code for hand gesture recognition.
- **`facial_expression_control/`**: Contains Python code for facial expression recognition.
- **`arduino_code/`**: Includes Arduino code to receive movement instructions from the laptop.

## **Instructions for Use**

1. **Setting up the Hardware:**
    - Assemble the robot car using the specified chassis, motors, motor driver, and switch.
    - Connect the Arduino Uno to the motor driver and power it using the battery.

2. **Running the Python Code:**
    - Navigate to the respective folders (`hand_gesture_control/` and `facial_expression_control/`) to run the Python scripts.
    - Install the necessary Python libraries specified in the requirements file.
    - Follow the instructions within each code file to configure the camera and execute the code for gesture or facial recognition.

3. **Uploading Arduino Code:**
    - Open the Arduino IDE and upload the code from the `arduino_code/` folder to the Arduino Uno.
    - Ensure the serial communication settings match between the Arduino code and the laptop.

4. **Connecting and Testing:**
    - Connect the laptop and Arduino Uno via a USB long wire (serial connection).
    - Run the Python code for gesture or facial recognition, and observe the movement of the robot car based on the recognized gestures or facial expressions.

## **Requirements**

Ensure you have the following Python libraries installed:

- **cv2 (OpenCV)**: Used for computer vision tasks, including image and video processing.
- **mediapipe**: A library for building machine learning pipelines for perception and understanding tasks, like hand tracking.
- **serial**: Required for serial communication with the Arduino Uno.

Install these libraries using the following commands:
```bash
pip install opencv-python
pip install mediapipe
pip install pyserial
```


## **Instructions for Use**

1. **Setting up the Hardware:**
    - Assemble the robot car using the specified chassis, motors, motor driver, and switch.
    - Connect the Arduino Uno to the motor driver and power it using the battery.

2. **Running the Python Code:**
    - Navigate to the respective folders (`hand_gesture_control/` and `facial_expression_control/`) to run the Python scripts.
    - Install the necessary Python libraries specified in the requirements file.
    - Follow the instructions within each code file to configure the camera and execute the code for gesture or facial recognition.

3. **Uploading Arduino Code:**
    - Open the Arduino IDE and upload the code from the `arduino_code/` folder to the Arduino Uno.
    - Ensure the serial communication settings match the Arduino code and the laptop.

4. **Connecting and Testing:**
    - Connect the laptop and Arduino Uno via a USB long wire (serial connection).
    - Run the Python code for gesture or facial recognition, and observe the movement of the robot car based on the recognized gestures or facial expressions.

## **Media Files**

- **Photos:**
    - [Robot Car Image](/Image-robo.jpg)
    
## **License**
This project is licensed under the MIT License - see the LICENSE.md file for details.

## **Future Development**
In the next stages of development, we plan to incorporate communication via RF modules or Bluetooth to enhance the robot's control and mobility.
