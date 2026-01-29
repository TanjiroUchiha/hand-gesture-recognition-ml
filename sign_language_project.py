import cv2
import mediapipe as mp
import numpy as np
import pickle

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))


cap = cv2.VideoCapture(0)
prev_gesture = ""

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            data = []
            for lm in hand_landmarks.landmark:
                data.extend([lm.x, lm.y])

            prediction = model.predict([np.asarray(data)])
            gesture = prediction[0]


            cv2.putText(frame, f"Gesture: {gesture}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Sign Language Translator", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


