import json
import urlparse
import os
import copy
import time
from random import randint
from image_converter import convert_image
from fishface_classifier import predict_emotion


TMP_IMAGE_STORAGE = './tmp_img_storage'

EMOTIONS_LIST = ['neutral', 'anger', 'disgust', 'happy', 'sadness', 'surprise']
NO_EMOTION = 'no_emotion'

def emotions_list():
    emotions = copy.copy(EMOTIONS_LIST)
    emotions.append(NO_EMOTION)
    return emotions

def recognize_emotion(json_data):
    data = json.loads(json_data)
    image = data['image']
    up = urlparse.urlparse(image)
    head, data = up.path.split(',', 1)

    cropped_face, face_detected = convert_image(data)
    if(face_detected):
        emotion = predict_emotion(cropped_face, EMOTIONS_LIST)
    else:
        emotion = NO_EMOTION

    return emotion
