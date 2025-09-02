import cv2
import numpy as np

img = cv2.imread("mykids.jpg")
cv2.resize(img, (200,200))
b,g,r = cv2.split(img)

blank1= np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)
cv2.imshow("orig", img)

while True:
    key = cv2.waitKey(0)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break  # Exit the loop

    elif key == ord("b"):
        cv2.imshow("orig", cv2.merge((b, blank1, blank1)))

    elif key == ord("r"):
        cv2.imshow("orig", cv2.merge((blank1, blank1, r)))

    elif key == ord("g"):
        cv2.imshow("orig", cv2.merge((blank1, g, blank1)))

    elif key == ord("o"):
        cv2.imshow("orig", cv2.merge((b, g, r)))
