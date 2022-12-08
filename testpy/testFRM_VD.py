import cv2
import numpy as np

def getFrames():
    video = cv2.VideoCapture('Lucas.mp4')
    ok, frame = video.read()
    count = 0
    while ok:
        cv2.imwrite("frame%d.jpg".format(count), frame)
        print('WRITTEN FRAME:',count)
        count+=1
        ok, frame = video.read()
    video.release()

getFrames()