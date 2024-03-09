import cv2

face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier(r"mouth.xml")
smile_cascade = cv2.CascadeClassifier(r"haarcascade_smile.xml")
fullbody_cascade = cv2.CascadeClassifier(r"haarcascade_fullbody.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img1 = cap.read()
    img = cv2.flip(img1, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fullbodies = fullbody_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in fullbodies:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "Full Body", (x, y), 1, cv2.FONT_HERSHEY_DUPLEX, (255, 0, 0), 2)

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

        # Region of interest for mouth detection within the face
        roi_mouth = gray[y+h//2:y+h, x:x+w]
        mouths = mouth_cascade.detectMultiScale(roi_mouth)
        for (mx, my, mw, mh) in mouths:
            cv2.rectangle(img, (x+mx, y+h//2+my), (x+mx+mw, y+h//2+my+mh), (0, 0, 255), 2)
            cv2.putText(img, "Mouth", (x+mx, y+h//2+my), 1, cv2.FONT_HERSHEY_DUPLEX, (0, 0, 255), 2)

        # Region of interest for smile detection within the face
        roi_smile = gray[y+h//2:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_smile)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (x+sx, y+h//2+sy), (x+sx+sw, y+h//2+sy+sh), (0, 255, 255), 2)
            cv2.putText(img, "Smile", (x+sx, y+h//2+sy), 1, cv2.FONT_HERSHEY_DUPLEX, (0, 255, 255), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
