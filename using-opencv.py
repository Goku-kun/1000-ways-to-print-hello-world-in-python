import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.putText(frame, 'Hello World', (frame.shape[0]//2,frame.shape[1]//2), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2) 
    cv2.imshow("Hello World", frame)


    if cv2.waitKey(1) == 27:
        break

cap.release()
