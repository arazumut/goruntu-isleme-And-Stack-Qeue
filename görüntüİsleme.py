import cv2

# Yüz, göz, ağız, gülümseme ve el cascade sınıflandırıcılarının dosya yolları
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier(r"mouth.xml")
smile_cascade = cv2.CascadeClassifier(r"haarcascade_smile.xml")
hand_cascade = cv2.CascadeClassifier(r"hand.xml")  # El cascade sınıflandırıcı eklendi

# Web kamerası yakalama
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()

    # Görüntüyü yatay çevir (isteğe bağlı)
    img = cv2.flip(img, 1)

    # Gri tonlamaya dönüştür
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Yüz algılama
    faces = face_cascade.detectMultiScale(gray, 1.4, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(img, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Göz algılama (yüz bölgesi içinde)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)
            cv2.putText(img, "Eye", (x+ex, y+ey-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Ağız algılama (yüz bölgesi içinde)
        roi_mouth = gray[y+h//2:y+h, x:x+w]
        mouths = mouth_cascade.detectMultiScale(roi_mouth)
        for (mx, my, mw, mh) in mouths:
            cv2.rectangle(img, (x+mx, y+h//2+my), (x+mx+mw, y+h//2+my+mh), (0, 0, 255), 2)
            cv2.putText(img, "Mouth", (x+mx, y+h//2+my-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Gülümseme algılama (yüz bölgesi içinde)
        roi_smile = gray[y+h//2:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_smile)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (x+sx, y+h//2+sy), (x+sx+sw, y+h//2+sy+sh), (0, 255, 255), 2)
            cv2.putText(img, "Smile", (x+sx, y+h//2+sy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Görüntüyü ekranda göster
    cv2.imshow("Face Detection", img)

    # 'q' tuşuna basılınca döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereyi kapat
cap.release()
cv2.destroyAllWindows()
