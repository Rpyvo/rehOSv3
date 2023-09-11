import os
import random
import requests
import sqlite3

version = "v3"

# SQLite veritabanı bağlantısı
conn = sqlite3.connect('YOURDATABASE.db') #KENDI DB YAZ!
cursor = conn.cursor()

# Tablo oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS command_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        command TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')
conn.commit()

def rehOS_random_number():
    return f"{random.randint(0, 3)}.{random.randint(1, 30)}.{random.randint(1, 60)}"

def register():
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")

    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))
    
    conn.commit()

def login():
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")

    cursor.execute('''
        SELECT * FROM users
        WHERE username = ? AND password = ?
    ''', (username, password))

    user = cursor.fetchone()

    if user:
        return user[1]  # Kullanıcının ismi
    else:
        return None

def hesapla():
    while True:
        print("Kullanılabilir İşlemler:")
        print("- toplama")
        print("- cikarma")
        print("- carpma")
        print("- bolme")
        print("- exit")
        operation = input(f"{current_user} >> ")

        if operation == "exit":
            break

        if operation in ["toplama", "cikarma", "carpma", "bolme"]:
            try:
                sayi1 = float(input("Lütfen ilk sayıyı giriniz: "))
                sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))

                if operation == "toplama":
                    sonuc = sayi1 + sayi2
                elif operation == "cikarma":
                    sonuc = sayi1 - sayi2
                elif operation == "carpma":
                    sonuc = sayi1 * sayi2
                elif operation == "bolme":
                    if sayi2 != 0:
                        sonuc = sayi1 / sayi2
                    else:
                        sonuc = "Sıfıra bölme hatası!"
                print(f"İşte sonuç: {sonuc}")
            except ValueError:
                print("Geçersiz giriş! Lütfen sayıları doğru formatta girin.")
        else:
            print(f"Hata: '{operation}' geçersiz bir işlem!")

def run_rehOS():
    global current_user
    user_name = rehOS_random_number()
    current_user = user_name  # Varsayılan olarak rastgele bir isim

    while True:
        command = input(f"rehOS\\user\\root@{user_name} >> ")

        if command == "exit":
            break
        elif command == "rhelp" or command == "help":
            print("Kullanılabilir Komutlar:")
            print("- rhelp: Komut listesini gösterir")
            print("- exit: rehOS'tan çıkış yaparsınız")
            print("- setName: Kullanıcı adını değiştirir")
            print("- editFile: Dosya oluşturur veya düzenler")
            print("- printOS <text>: Yazı yazdırır mesela (printOS Hello World)")
            print("- hesapla: Hesaplama işlemi yapar")
            print("- checkUpdate: Güncelleme kontrolü yapar")
            print("- register: Yeni bir hesap oluşturur")
            print("- login: Mevcut bir hesap ile giriş yapar")
        elif command == "setName":
            user_name = rehOS_random_number()
            current_user = user_name
            print(f"Kullanıcı adınız başarıyla değiştirildi: root@{user_name}")
        elif command == "editFile":
            file_name = input("Dosya adı: ")
            content = input("Dosya içeriği: ")
            try:
                with open(file_name, "w") as file:
                    file.write(content)
                    print(f"Dosya başarıyla kaydedildi: {file_name}")
            except Exception as e:
                print(f"Dosya kaydedilirken hata oluştu: {e}")
        elif command == "hesapla":
            hesapla()
        elif command == "checkUpdate":
            start_update()  # Güncelleme kontrolü yap
        elif command == "register":
            register()  # Yeni bir hesap oluştur
        elif command == "login":
            user = login()
            if user:
                current_user = user
                print(f"Başarıyla giriş yapıldı: root@{user}")
            else:
                print("Hatalı kullanıcı adı veya şifre.")
        elif command.startswith("printOS"):
            text = command.split(" ", 1)[1]
            print(text)
            save_command_to_history(command)  # Komutu geçmişine ekle
        else:
            print(f'Hata: "{command}" Komutu bulunamadı')

def start_update():
    url = "https://rehos.reshyy.repl.co"  
    response = requests.get(url)

    if response.text == version :
        pass # Güncelleme yoksa hiçbir şey yapma
    else:
        print(f"Uygulamada güncelleme var! {response.text} Sürümü yayınlandı!")

def update():
    url = "https://rehos.reshyy.repl.co"  
    response = requests.get(url)

    if response.text == version :
        print("Uygulamada güncelleme yok")
    else:
        print(f"Uygulamada güncelleme var! {response.text} Sürümü yayınlandı!")

if __name__ == "__main__":
    command_history = []  # Komut geçmişi listesi
    current_user = None  # Şu anki kullanıcı ismi
    current_user_id = None  # Şu anki kullanıcının IDsi (SQLite veritabanındaki)
    
    print("==================== rehOS işletim sistemine hoş geldiniz ====================")
    start_update()  # Uygulama başladığında güncelleme kontrolü yap
    print("")
    run_rehOS()
