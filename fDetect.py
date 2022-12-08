from distutils.command.config import config
import numpy as np
import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = grey[y:y+h, x:x+w] #[cord1 - height , cord2 - height]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf =recognizer.predict(roi_gray)
        if conf>=45 and conf<=85:
            print(id_)
            
        img_item = "my-image,jpeg"
        cv2.imwrite(img_item, roi_gray)


    cv2.imshow('test', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    