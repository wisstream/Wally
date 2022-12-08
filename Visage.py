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

def visage(per_rechercher, i, y, video):
    KEY = "93a3729d3e174389817f807e1b184e7e"
    ENDPOINT = "https://wally.cognitiveservices.azure.com/"
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
