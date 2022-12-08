from array import array
import asyncio
from distutils.command.build_scripts import first_line_re
import io
import glob
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
# from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition

import os
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import numpy as np
import cv2
from typing import Text
from Visage import visage
from Detection import Detection
from Reconnaissance import Reconaissance

 
global Detection_visage
global numero

def main(i,y,per_rechercher):
    
    first_image_face_ID = Detection(per_rechercher, 1)
   
    while(y < i):
        multi_face_image_url = open('screen'+str(y)+'.jpg', "rb")
        multi_image_name = os.path.basename("/")
       
        second_image_face_IDs = Detection(multi_face_image_url, 2)
        Reconaissance(first_image_face_ID,second_image_face_IDs,multi_face_image_url)
       
        y +=25

cap = cv2.VideoCapture('105_c.mp4')
i = 0
y = 0
x = 0
maximage=3
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i % 25 == 0:
        cv2.imwrite('screen'+str(i)+'.jpg', frame)
    i += 1
cap.release()
cv2.destroyAllWindows()

while(x<maximage):
    print('eleve'+str(x))
    tete = open('eleve'+str(x)+'.jpg', "rb")
    main(i,y,tete)
    x +=1