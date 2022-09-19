import cv2
from handUtil import HandDetector

## camera setup
camera = cv2.VideoCapture(0)
hand_detector = HandDetector()

while True:
     success, img = camera.read()

     if success:
          img = cv2.flip(img, 1)
          hand_detector.process(img)
          position =  hand_detector.find_positions(img)
          left_index_finger = position['Left'].get(8,None)
          right_index_finger = position['Right'].get(8,None)

          if left_index_finger:
               cv2.circle(img, (left_index_finger[0], left_index_finger[1]), 20, (0, 0, 255), cv2.FILLED)

          if right_index_finger:
               cv2.circle(img, (right_index_finger[0], right_index_finger[1]), 20, (0, 0, 255), cv2.FILLED)

          cv2.imshow("Vedio", img)

     ## type kebord q to quit
     quit = cv2.waitKey(1)
     if quit == ord('q'):
          break

## release camera
camera.release()
cv2.destroyAllWindows()


