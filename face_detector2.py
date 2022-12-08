from cgitb import grey
import cv2
from cv2 import imread
import sys
from random import randrange 


sys.path.append('/usr/local/lib/python2.7.16/site-packages')

#data pre-trained img
trained_face_data = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') 
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
# img to detect
#img = cv2.imread('BG.jpeg')

#cature img by webcam 
#0= webcam sinon mettre ('nomde la video.mp4')
webcam = cv2.VideoCapture(0)

#frame infit 
while True:

    successful_frame_read, frame = webcam.read()

# key = cv2.waitKey(1)

    # turn img to grey 
    greyscaled_img =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect face
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    #dessigner le rectangle de mainiere auto 
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),5)



    cv2.imshow('test', frame)
    key = cv2.waitKey(1)
 
    if key==81 or key==113:
        break
webcam.release()
webcam.destroyAllWindows()

#x,y),(x+w,y+h
# dessigne le rectangle autour du visage 
#cv2.rectangle(img,(204,288),(204+348,288+348),(0,255,0),2)
'''


#display img w faces 


# print les cooredonnee du rectangle qui entoure le visage 
#print(face_coordinates)
#

'''
print("Code completed")