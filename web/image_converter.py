import cv2
import numpy as np

FACECASCADE = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")

def convert_image(image_data):
    nparr = np.fromstring(image_data.decode('base64'), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # adaptive equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    # face detection
    face = FACECASCADE.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=20, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw rectangle around detected faces
    for (x, y, w, h) in face:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 0), 2)

    if len(face) == 1:
        face_slice = crop_face(clahe_image, face)
        face_detected = True
    else:
        face_slice = None
        print("no face or multiple faces detected")
        face_detected = False

    return face_slice, face_detected


def crop_face(image, face): #Crop face
    for (x, y, w, h) in face:
        face_slice = cv2.resize(image[y:y+h, x:x+w], (350, 350))
    return face_slice