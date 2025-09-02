import cv2
import datetime

cap = cv2.VideoCapture(0)
print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 600)
cap.set(4, 800)
print("Width====",cap.get(3))
print("Height===",cap.get(4))

writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"), 20, (640, 480), 1)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3))
       date_data = "Date: "+str(datetime.datetime.now())
       frame = cv2.putText(frame, text, (10, 20), font, 1,
                           (0, 155, 255), 1, cv2.LINE_AA)
       frame = cv2.putText(frame, date_data, (20, 50), font, 1,
                           (100, 255, 255), 1, cv2.LINE_AA)
       cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
       cv2.imshow('frame', frame)
       writer.write(frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()



