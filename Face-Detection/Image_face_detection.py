import cv2 as cv
img = cv.imread("Photos/group2.jpg")
img = cv.resize(img, (1280, 720))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


face_detector = cv.CascadeClassifier('haar_face.xml')
eye_detector = cv.CascadeClassifier('haarcascade_eye.xml')
face = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for(x, y, w, h) in face:
    # Marking the face with rectangle
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # extracting the region of interest for detect eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

# passing the gray region to detect eyes
eyes = eye_detector.detectMultiScale(roi_gray)
for(ex, ey, ew, eh) in eyes:
    # Marking the eyes with rectangle
    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

# Add number of faces text on image 
face_count_text = f"Face Detected: {len(face)}"
cv.putText(img, face_count_text, (30, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

print(f"NO. of faces found = {len(face)}")
cv.imshow("Detected Faces", img)
cv.waitKey(0)
cv.destroyAllWindows()
