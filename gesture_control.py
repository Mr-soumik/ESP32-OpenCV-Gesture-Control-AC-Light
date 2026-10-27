import cv2
import mediapipe as mp
import serial
import time

# Configure the Serial Port. Change 'COM3' to match your ESP32's port.
SERIAL_PORT = "COM3"  
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for connection to establish
    print(f"Connected to ESP32 on {SERIAL_PORT}")
except Exception as e:
    print(f"Error connecting to serial port: {e}")
    exit()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]
cap = cv2.VideoCapture(0)
last_state = None

def send_command(command_char):
    global last_state
    if command_char != last_state:
        ser.write(command_char.encode('utf-8'))
        last_state = command_char
        state_str = "ON" if command_char == 'H' else "OFF"
        print(f"Sent command: {state_str}")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            fingers_up = 0
            for id in range(1, 5):
                if landmarks[tip_ids[id]].y < landmarks[tip_ids[id] - 2].y:
                    fingers_up += 1

            if fingers_up >= 4:
                cv2.putText(img, "STATE: LIGHT ON", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                send_command('H')
            elif fingers_up <= 1:
                cv2.putText(img, "STATE: LIGHT OFF", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                send_command('L')

    cv2.imshow("Hand Gesture AC Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
