import pyautogui as p
import cv2
import numpy as np

rs = p.size()
fps = 60
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output2.avi", fourcc, fps, rs, 0)
count = 0
print(rs)
while True:
    ss = p.screenshot()
    opencv_ss = cv2.cvtColor(np.array(ss), cv2.COLOR_BGR2GRAY)
    padam = cv2.resize(opencv_ss, (192,108)) 
    output_file.write(opencv_ss)
    cv2.imshow("recording..", padam)
    if (cv2.waitKey(1) & 0xff == ord('q')):
        break
