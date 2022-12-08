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




def Reconaissance(first_image_face_ID,second_image_face_IDs, visage):
    KEY = "93a3729d3e174389817f807e1b184e7e"
    ENDPOINT = "https://wally.cognitiveservices.azure.com/"
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    # print('0')
    # Visage = face_client.face.detect_with_stream(image= visage, detection_model='detection_03')
    # print("test1")
    similar_faces = face_client.face.find_similar(face_id=first_image_face_ID, face_ids=second_image_face_IDs)   
    # print("test2")

    for face in similar_faces:
         first_image_face_ID = face.face_id
        #  face_info = next(x for x in Visage if x.face_id == first_image_face_ID)
         print('vous etes sur la video')
         return 0
    print("L'eleve n'est pas sur la video")
