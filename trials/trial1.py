import cv2

padam = cv2.imread("mykids.jpg",0)
#padam = cv2.resize(padam,(50,50))
padam = cv2.flip(padam, 1)
while True:
    cv2.imshow("this padam", padam)
    k = cv2.waitKey(0) & 0xFF
    if k == ord("q"):
        cv2.destroyAllWindows()
        break
    elif k == ord("s"):
        cv2.imwrite("output.png", padam)
        cv2.destroyAllWindows()
        break
