import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("output.mp4",fourcc,20,(640,480),1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    flipped = cv2.flip(frame, 0)
    output.write(flipped)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break