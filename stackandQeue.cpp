stack = []
queue = []

def stack_menu() :
    """Stack işlemleri için menü fonksiyonu."""
    while True :
        print("\nStack İşlemleri Menüsü:")
        print("1. Ekle")
        print("2. Bul ve Sil")
        print("3. Bul ve Göster")
        print("4. Tümünü Listele")
        print("5. Ana Menüye Dön")

        secim = input("Seçiminizi giriniz: ")

        if secim == "1":
stack_ekle()
elif secim == "2" :
    stack_bul_sil()
    elif secim == "3" :
    stack_bul_goster()
    elif secim == "4" :
    stack_listele()
    elif secim == "5" :
    break
        else:
print("Geçersiz seçim!")

def stack_ekle() :
    """Stack'e eleman ekleme fonksiyonu."""
    deger = input("Eklemek istediğiniz değeri giriniz: ")
    stack.append(deger)
    print(f"{deger} değeri stack'e eklendi.")

    def stack_bul_sil() :
    """Stack'te bir eleman bulup silme fonksiyonu."""
    bulunacak = input("Bulmak istediğiniz değeri giriniz: ")
    if bulunacak in stack :
stack.remove(bulunacak)
print(f"{bulunacak} değeri stack'ten silindi.")
    else:
print(f"{bulunacak} değeri stack'te bulunamadı.")

def stack_bul_goster() :
    """Stack'te bir eleman bulup gösterme fonksiyonu."""
    bulunacak = input("Bulmak istediğiniz değeri giriniz: ")
    if bulunacak in stack :
print(f"{bulunacak} değeri stack'te bulunmaktadır.")
    else :
        print(f"{bulunacak} değeri stack'te bulunamadı.")

        def stack_listele() :
        """Stack'teki tüm elemanları listeleme fonksiyonu."""
        if stack :
            print("Stack'teki elemanlar:")
            for deger in stack :
print(deger)
        else:
print("Stack boş.")

def queue_menu() :
    """Queue işlemleri için menü fonksiyonu."""
    while True :
        print("\nQueue İşlemleri Menüsü:")
        print("1. Ekle")
        print("2. Kaldır")
        print("3. En Önde Ne Var?")
        print("4. Tümünü Listele")
        print("5. Ana Menüye Dön")

        secim = input("Seçiminizi giriniz: ")

        if secim == "1":
queue_ekle()
elif secim == "2" :
    queue_kaldir()
    elif secim == "3" :
    queue_on_eleman()
    elif secim == "4" :
    queue_listele()
    elif secim == "5" :
    break
        else:
print("Geçersiz seçim!")

def queue_ekle() :
    """Queue'ya eleman ekleme fonksiyonu."""
    deger = input("Eklemek istediğiniz değeri giriniz: ")
    queue.append(deger)
    print(f"{deger} değeri queue'ya eklendi.")

    def queue_kaldir() :
    """Queue'dan eleman kaldırma fonksiyonu."""
    if queue :
        kaldirilan = queue.pop(0)
        print(f"{kaldirilan} değeri queue'dan silindi.")
    else :
        print("Queue boş.")

        def queue_on_eleman() :
        """Queue'nun en önündeki elemanı gösterme fonksiyonu."""
        if queue :
            print(f"Queue'nun en önündeki eleman: {queue[0]}")
        else :
            print("Queue boş.")

            def queue_listele() :
            """Queue'deki tüm elemanları listeleme fonksiyonu."""
            if queue :
                print("Queue'daki elemanlar:")
                for deger in queue :
print(deger)
            else:
print("Queue boş.")

stack_menu()

