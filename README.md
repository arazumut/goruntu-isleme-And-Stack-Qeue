<h1>ağız,göz,yüz,gülümseme,el ve full vücut algılayan görüntü işleme kodu</h1>

Bu Python kodu, bir bilgisayar kamerası kullanarak yüz, göz, ağız ve gülümseme tespiti yapar 
    İlk olarak, gerekli kütüphaneler (cv2) içe aktarılır. Ayrıca, yüz, göz, ağız, gülümseme ve el tespiti için önceden eğitilmiş sınıflandırıcılar (CascadeClassifier) belirtilen XML dosyalarından yüklenir.

    cv2.VideoCapture(0) ile bir video yakalama cihazı başlatılır. Parametre olarak 0, bilgisayarınıza bağlı olan birincil kamerayı belirtir.

    Sonsuz bir döngü (while) başlatılır. Bu döngü, kameradan sürekli görüntüler alır ve her bir kare üzerinde yüz, göz, ağız, gülümseme ve el tespiti yapar.

    cap.read() işleviyle bir sonraki kare alınır ve ret ve img değişkenlerine atılır. ret değeri, kameradan kare alınıp alınamadığını gösterir. img, alınan kareyi temsil eden bir görüntü dizisidir.
 
    Görüntü yatay olarak (cv2.flip()) çevrilir. Bu, aynı anda hem kameranın ön hem de arka tarafından tespitlerin daha iyi yapılabilmesini sağlar.

    Görüntü siyah-beyaza (gray) formata dönüştürülür. Yüz, göz, ağız, gülümseme ve el tespiti, genellikle siyah-beyaz görüntülerde daha iyi çalışır.

    face_cascade.detectMultiScale() işlevi, yüzleri tespit eder. gray görüntüsüne uygulanır ve tespit edilen yüzlerin dikdörtgen koordinatlarını (x, y, w, h) verir.

    Her bir tespit edilen yüz için, gözlerin (eye_cascade.detectMultiScale()), ağızların (mouth_cascade.detectMultiScale()) ve gülümsemelerin (smile_cascade.detectMultiScale()) tespiti yapılır. Her bir tespit edilen öğe için dikdörtgenler çizilir ve etiketlenir.

    El tespiti için benzer bir işlem yapılır (hand_cascade.detectMultiScale()).

    Etiketler ve dikdörtgenler, cv2.putText() ve cv2.rectangle() işlevleri kullanılarak orijinal görüntü üzerine çizilir.

    cv2.imshow() işleviyle, tespit edilen yüzlerin, gözlerin, ağızların, gülücüklerin ve ellerin işaretli olduğu orijinal görüntü görüntülenir.

    cv2.waitKey() işlevi, bir tuşa basılmasını bekler. Eğer basılan tuş 'q' ise (ord('q')), döngüden çıkılır ve program sonlanır.

    Kamera yakalaması (cap.release()) serbest bırakılır ve tüm penceler kapatılır (cv2.destroyAllWindows()).

Bu kod, OpenCV (cv2) kütüphanesi kullanılarak yüz, göz, ağız, gülümseme ve el tespiti işlemlerini gerçekleştirir ve tespit edilen nesneleri orijinal görüntü üzerinde işaretler.





    stack_menu() Fonksiyonu:
        Bu fonksiyon, kullanıcıya bir "stack" (yığın) veri yapısı üzerinde çeşitli işlemler yapma seçenekleri sunan bir menü görüntüler.
        Kullanıcı bu menüden işlem seçtikçe ilgili işlevlere yönlendirilir.

    stack_ekle() Fonksiyonu:
        Kullanıcıya bir değer girmesini isteyerek, bu değeri "stack" veri yapısına ekler.
        Eklenen değeri kullanıcıya doğrulama amacıyla geri bildirim olarak gösterir.

    stack_bul_sil() Fonksiyonu:
        Kullanıcıdan bir değer girmesini ve bu değerin "stack" içinde varsa onu kaldırmasını ister.
        Girilen değerin "stack" içinde bulunup bulunmadığını kontrol eder, varsa kaldırır ve kullanıcıya geri bildirim gösterir.

    stack_bul_goster() Fonksiyonu:
        Kullanıcıdan bir değer girmesini ister ve bu değerin "stack" içinde olup olmadığını kontrol eder.
        Eğer değer "stack" içinde bulunuyorsa bu bilgiyi kullanıcıya gösterir.

    stack_listele() Fonksiyonu:
        "Stack" veri yapısındaki tüm elemanları listeleyen bir fonksiyondur.
        Eğer "stack" boşsa, buna ilişkin bir bildirim gösterir.

    queue_menu() Fonksiyonu:
        Benzer şekilde "queue" (kuyruk) veri yapısı üzerinde çeşitli işlemler yapma seçenekleri sunan bir menü gösterir.

    queue_ekle() Fonksiyonu:
        Kullanıcıdan bir değer alarak bu değeri "queue" veri yapısına ekler.
        Eklenen değeri kullanıcıya doğrulama amacıyla geri bildirim olarak gösterir.

    queue_kaldir() Fonksiyonu:
        "Queue" veri yapısından bir öğe kaldırır.
        Eğer "queue" boşsa, buna ilişkin bir bildirim gösterir.

    queue_on_eleman() Fonksiyonu:
        "Queue" veri yapısının en önündeki elemanı gösterir.
        Eğer "queue" boşsa, buna ilişkin bir bildirim gösterir.

    queue_listele() Fonksiyonu:
        "Queue" veri yapısındaki tüm elemanları listeleyen bir fonksiyondur.
        Eğer "queue" boşsa, buna ilişkin bir bildirim gösterir.

Kod, kullanıcıya stack ve queue veri yapıları üzerinde çeşitli işlemler yapma imkanı sunar ve kullanıcının seçimlerine göre ilgili işlevleri gerçekleştirir.

![Ekran görüntüsü 2024-05-13 130906](https://github.com/arazumut/goruntu-isleme-And-Stack-Qeue/assets/150933483/a6d584e5-e37d-48f9-a762-3003d141e075)

![Ekran görüntüsü 2024-05-13 130833](https://github.com/arazumut/goruntu-isleme-And-Stack-Qeue/assets/150933483/c9d395cc-5ffe-4959-8d29-a88fd2f4e97b)
![Ekran görüntüsü 2024-05-13 130818](https://github.com/arazumut/goruntu-isleme-And-Stack-Qeue/assets/150933483/89f3c92c-a465-49f3-9f2b-162b90b8582a)
