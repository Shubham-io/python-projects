from sre_constants import SUCCESS
import cv2 as cv
from cv2 import waitKey
from cv2 import rectangle

face_detector = cv.CascadeClassifier('haar_face.xml')
eye_detector = cv.CascadeClassifier('haarcascade_eye.xml')
cap = cv.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv.resize(img, (1280, 720))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)  # face has specific quardinates
    for(x, y, w, h) in face:
        # To draw rectangle around face
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = img[y:y+h, x:x+h]
        eyes = eye_detector.detectMultiScale(
            roi_gray)  # eyes has specific quardinates
        for(ex, ey, ew, eh) in eyes:
            # To draw rectangle around eyes
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 3)
    cv.imshow("Detected Faces", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# cv.destroyAllWindows()
