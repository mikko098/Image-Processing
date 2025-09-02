import cv2
import numpy as np
img = cv2.imread("logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,127,255,0)
#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("Hierarchy==\n",hier)

#drawcontour(img,cnts,id of contour,color,thickness)#here if we draw all
#contour just pass -1
#Draw the contours
img3= cv2.drawContours(img,cnts,-1,(176,10,15),4)


#ouput----
cv2.imshow("original===",img)
cv2.imshow("contours===",img3)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllwindow()