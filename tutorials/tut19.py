import pafy
import cv2

url = "https://youtu.be/sRFM5IEqR2w"
cap = cv2.VideoCapture(url)

ret, frame = cap.read()
while ret != False:
    cv2.imshow("win", frame)
    ret, frame = cap.read()