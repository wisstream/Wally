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

def Detection(per_rechercher, compteur):
    #fonction detection visage 
    KEY = "93a3729d3e174389817f807e1b184e7e"
    ENDPOINT = "https://wally.cognitiveservices.azure.com/"
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    Detection_visage = face_client.face.detect_with_stream(image= per_rechercher, detection_model='detection_03')
    if not Detection_visage:
        print("Pas de visage sur l'image",  per_rechercher)
    if compteur == 2:
        first_image_face_ID = list(map(lambda x: x.face_id, Detection_visage))
    else:
        first_image_face_ID = Detection_visage[0].face_id
    return(first_image_face_ID)
    # print(first_image_face_ID)