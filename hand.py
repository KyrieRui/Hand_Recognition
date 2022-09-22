import cv2
from handUtil import HandDetector
import time
import numpy as np
import math
import applescript
########################################
wCam, hCam = 1280, 720
volum_range_min = 0
volum_range_max = 100
target_volume = 50
target_volume_bar = 400
volume_percent = 0
########################################
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
          left_thump = position['Left'].get(4,None)
          right_thump = position['Right'].get(4,None)

          cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)

          if left_index_finger:
               cv2.circle(img, (left_index_finger[0], left_index_finger[1]), 20, (0, 0, 255), cv2.FILLED)
               cv2.putText(img, 'Left', (left_index_finger[0], left_index_finger[1]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

          if left_thump:
                cv2.circle(img, (left_thump[0], left_thump[1]), 20, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, 'Left_thum', (left_thump[0], left_thump[1]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                x_left_1 = left_index_finger[0]
                y_left_1 = left_index_finger[1]
                x_left_2 = left_thump[0]
                y_left_2 = left_thump[1]
                cx_left = (x_left_1 + x_left_2) // 2
                cy_left = (y_left_1 + y_left_2) // 2

                cv2.line(img, (x_left_1, y_left_1), (x_left_2, y_left_2), (255, 0, 255), 3)

                length_left = math.hypot(x_left_2 - x_left_1, y_left_2 - y_left_1)
                # Hand range 50 - 300
                # Volume Range 0 - 100
                target_volume = np.interp(length_left, [50, 300], [volum_range_min, volum_range_max])
                target_volume_bar = np.interp(length_left, [50, 300], [400, 150])
                volume_percent = np.interp(length_left, [50, 300], [0, 100])
                cv2.rectangle(img, (50, int(target_volume_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(volume_percent)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                applescript.tell.app('System Events', 'set volume output volume {}'.format(target_volume))


          if right_index_finger:
               cv2.circle(img, (right_index_finger[0], right_index_finger[1]), 20, (0, 0, 255), cv2.FILLED)
               cv2.putText(img, 'Right', (right_index_finger[0], right_index_finger[1]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

          if right_thump:
               cv2.circle(img, (right_thump[0], right_thump[1]), 20, (0, 0, 255), cv2.FILLED)
               cv2.putText(img, 'Right_thum', (right_thump[0], right_thump[1]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
               x_right_1 = right_index_finger[0]
               y_right_1 = right_index_finger[1]
               x_right_2 = right_thump[0]
               y_right_2 = right_thump[1]
               cx_right = (x_right_1 + x_right_2) // 2
               cy_right = (y_right_1 + y_right_2) // 2

               cv2.line(img, (x_right_1, y_right_1), (x_right_2, y_right_2), (255, 0, 255), 3)

          cv2.imshow("Vedio", img)

          # cv2.rectangle(img, (50, int(target_volume_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

     ## type kebord q to quit
     quit = cv2.waitKey(1)
     if quit == ord('q'):
          break

## release camera
camera.release()
cv2.destroyAllWindows()


