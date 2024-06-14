import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
indez_y =0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=[0, 255, 0])
                    indez_x = screen_width/frame_width*x
                    indez_y = screen_height/frame_height*y
                    pyautogui.moveTo(indez_x, indez_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=[0, 255, 0])
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print("outside:", abs(indez_y - thumb_y))
                    if abs(indez_y - thumb_y) < 25:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print("clicked!")
    cv2.imshow('virtual hand', frame)
    cv2.waitKey(1)




