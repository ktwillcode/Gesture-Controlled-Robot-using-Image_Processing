import cv2
import serial

# Load pre-trained Haar Cascade classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize video capture from the default webcam
video_capture = cv2.VideoCapture(0)

# Initialize serial communication with Arduino
ser = serial.Serial('COM8', 9600, timeout=1)  # Change 'COM3' to the appropriate port

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face and smile detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate through detected faces
    for (x, y, w, h) in faces:
        # Draw rectangles around the detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Get the region of interest (ROI) for smile detection within the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect smiles within the detected face region
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

        # If a smile is detected, send 'F' to Arduino; otherwise, send 'S'
        if len(smiles) > 0:
            cv2.putText(frame, 'Forward', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            ser.write(b'F')  # Send 'F' to Arduino
        else:
            cv2.putText(frame, 'Stop', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            ser.write(b'S')  # Send 'S' to Arduino

    # Display the resulting frame
    cv2.imshow('Smile Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object, close all windows, and close serial communication
video_capture.release()
cv2.destroyAllWindows()
ser.close()  # Close the serial connection
