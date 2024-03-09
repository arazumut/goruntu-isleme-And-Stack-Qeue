import cv2

face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img1 = cap.read()
    img = cv2.flip(img1, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.4, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(img, "Face", (x, y), 1, cv2.FONT_HERSHEY_DUPLEX, (0, 255, 0), 3)

        # Region of interest for eye detection within the face
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)
            cv2.putText(img, "Eye", (x+ex, y+ey), 1, cv2.FONT_HERSHEY_DUPLEX, (255, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
