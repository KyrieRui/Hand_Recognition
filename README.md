## Hand Detector
### Author: Ray
### Date: 09/20/2022
### Description: This is a hand detector using OpenCV and Mediapipe

#### This program basically detects the hand and the landmarks of the hand.
![Hand Detector](https://github.com/KyrieRui/Hand_Recognition/blob/main/Kapture%202022-09-20%20at%2014.08.16.gif)

## Installation
### Install OpenCV
```bash
pip install opencv-python
```

### Install Mediapipe
```bash
pip install mediapipe
```

#### If you are use M1 Mac, you can use this command to install Mediapipe
```bash
pip install mediapipe-silicon
```

## Usage
1. import two packages
```python
import cv2
import mediapipe as mp
```

2. allow the camera and hand solution in mediapipe
```python
camera = cv2.VideoCapture(0) ## '0' is your device default camera, use '1' if you have another camera
hand_detetor = mp.solutions.hands
```

3. We can def an loop, as long as the camera is open, we can get the image from the camera
```python
while True:
    success, img = camera.read()
    if success:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) ## because the mediapipe only support RGB image we need to convert it to RGB
        results = hand_detetor.process(img_rgb) ## get the hand result
        
        if results.multi_hand_landmarks: ## if we can detect the hand
            for hand_landmarks in results.multi_hand_landmarks: ## we can get the hand landmarks
                mp.solutions.drawing_utils.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS) ## draw the hand landmarks
        
        cv2.imshow("Hand Detector", img)
    quit = cv2.waitKey(1)

    if quit == ord('q'):
        break
```

4. Last step, we need to release the camera and destroy the window to save the device memory use
```python
camera.release()
cv2.destroyAllWindows()
```


## Reference
https://www.bilibili.com/video/BV1mb4y1B78p?vd_source=9fa62e123b591fe30734493ac73e11b1
