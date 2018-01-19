import json
import urlparse
import os
import copy
import time
from random import randint
from image_converter import convert_image
from fishface_classifier import predict_emotion


TMP_IMAGE_STORAGE = './tmp_img_storage'
# IMAGE_FILE = TMP_IMAGE_STORAGE + '/img.jpg'

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
    plain_data = data.decode("base64")

    if not os.path.exists(TMP_IMAGE_STORAGE):
        os.makedirs(TMP_IMAGE_STORAGE)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    IMAGE_FILE = TMP_IMAGE_STORAGE + '/img'+ timestr +'.jpg'
    with open(IMAGE_FILE, 'wb') as f:
        f.write(plain_data)

    cropped_face, face_detected = convert_image(TMP_IMAGE_STORAGE, IMAGE_FILE)
    if(face_detected):
        emotion = predict_emotion(cropped_face, EMOTIONS_LIST)
    else:
        emotion = NO_EMOTION

    # remove temporarily saved image from TMP_IMAGE_STORAGE
    remove_file(os.path.join(TMP_IMAGE_STORAGE, IMAGE_FILE))


    return emotion



def directory_cleanup(directory_path):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def remove_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
