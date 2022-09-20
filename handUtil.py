import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self):
        self.hand_detetor = mp.solutions.hands.Hands()
        self.hand_drawer = mp.solutions.drawing_utils

    def process(self, img):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.hands_data = self.hand_detetor.process(img_rgb)

        if self.hands_data.multi_hand_landmarks:
            for hand_landmark in self.hands_data.multi_hand_landmarks:
                self.hand_drawer.draw_landmarks(img, hand_landmark, mp.solutions.hands.HAND_CONNECTIONS)

    def find_positions(self, img):
        h, w, c = img.shape
        positions = {'Left': {}, 'Right': {}}
        if self.hands_data.multi_hand_landmarks:
            i = 0
            for hand_point in self.hands_data.multi_handedness:
                score = hand_point.classification[0].score
                if score > 0.7:
                    label = hand_point.classification[0].label
                    hand_lms = self.hands_data.multi_hand_landmarks[i].landmark
                    for id, lm in enumerate(hand_lms):

                        x, y = int(lm.x * w), int(lm.y * h)
                        positions[label][id] = (x, y)

                i = i + 1
        return positions

