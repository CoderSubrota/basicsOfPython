import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("The webcam is not defined !!")
else:
    while True:
     readCam, frame = cap.read()
     
     if readCam:
         cv2.imshow("Webcam Feed", frame)
     else:
         print("Error detected to open the web camera !!")
         break
     if cv2.waitKey(1) & 0xFF == ord("q"):
         break
cap.release()
cv2.destroyAllWindows()
