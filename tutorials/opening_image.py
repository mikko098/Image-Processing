import cv2
img1 = cv2.imread("thor.jpg",0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1
cv2.imshow("this padam", img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("ouput.png",img1)  #it accept name of image and data
    cv2.destroyAllWindows()