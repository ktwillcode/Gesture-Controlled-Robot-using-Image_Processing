import cv2
import mediapipe as mp
import serial

# Function to count fingers
def count_fingers(hand_landmarks):
    if hand_landmarks is None:
        return 0

    tip_ids = [4, 8, 12, 16, 20]  # Landmark IDs for finger tips

    fingers_open = 0
    # Thumb as a special case (different landmark points)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    
    if hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y:
        fingers_open += 1

    # Count fingers (other than thumb)
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers_open += 1

    return fingers_open

# Create a MediaPipe HandLandmarker object
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

# Open serial port for Arduino communication (change 'COM8' to your Arduino port)
ser = serial.Serial('COM8', 9600, timeout=1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

            finger_count = count_fingers(hand_landmarks)
            cv2.putText(frame, f'Finger Count: {finger_count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

            # Print and send commands to Arduino based on finger count
            if finger_count == 1:
                print("Sending command: F (Forward)")
                ser.write(b'F')  # Send 'F' for 1 finger
            elif finger_count == 2:
                print("Sending command: B (Backward)")
                ser.write(b'B')  # Send 'B' for 2 fingers
            # Add more print statements and conditions for other finger counts
            elif finger_count == 3:
                print("Sending command: R (Right)")
                ser.write(b'R')  # Send 'R' for 3 fingers
            elif finger_count == 4:
                print("Sending command: L (Left)")
                ser.write(b'L')  # Send 'L' for 4 fingers
            else:
                print("Sending command: S (Stop)")
                ser.write(b'S')  # Send 'S' for 0 or 5 fingers           
            while ser.in_waiting:
                response = ser.readline().decode().strip()
                print("Arduino response:", response)

            #time.sleep(1)  #
    cv2.imshow("Hand Landmarks", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
ser.close()

