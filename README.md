# rehOS İşletim Sistemi kabuğu ( Kısaca Bash gibi )

Bu, basit bir komut satırı tabanlı işletim sistemi simülasyonudur.

## Kullanılan Teknolojiler ve Modüller

- Python
- SQLite
- requests

## Nasıl Kullanılır

1. **Başlangıç**
   - `python main.py` komutu ile işletim sistemi başlatılır.

2. **Kullanıcı İşlemleri**
   - `register`: Yeni bir hesap oluşturur.
   - `login`: Mevcut bir hesap ile giriş yapar.

3. **Kullanılabilir Komutlar**
   - `rhelp` veya `help`: Komut listesini gösterir.
   - `exit`: rehOS'tan çıkış yaparsınız.
   - `setName`: Kullanıcı adını değiştirir.
   - `editFile`: Dosya oluşturur veya düzenler.
   - `printOS <text>`: Yazı yazdırır (örneğin `printOS Hello World`).
   - `hesapla`: Hesaplama işlemi yapar.
   - `checkUpdate`: Güncelleme kontrolü yapar.
   - `register`: Yeni bir hesap oluşturur.
   - `login`: Mevcut bir hesap ile giriş yapar.

4. **Hesaplama İşlemleri**
   - `toplama`, `cikarma`, `carpma`, `bolme`: İlgili işlemi yapar.

5. **Güncelleme Kontrolü**

   Uygulamadaki güncellemeler [rehOS web sitesi](https://rehos.reshyy.repl.co) üzerinden kontrol edilir.

   - Uygulama başladığında otomatik olarak güncelleme kontrolü yapılır.
   - Eğer yeni bir güncelleme mevcutsa, kullanıcıya bilgi verilir.
   - Sadece v1, v2 gibi kelimeleri algılar

6. **Kendi Web Siteniz ile Güncelleme Bağlantısı**

   Eğer kendi web siteniz üzerinden güncelleme kontrolü yapmak istiyorsanız, aşağıdaki adımları takip edebilirsiniz:

   - `start_update()` fonksiyonunda, `url` değişkenini kendi web sitenizin URL'si ile değiştirin.
   - projenin ilk başında olan versionla web sitedeki versiyon aynı olursa güncelleme bildirimi kullanıcı almaz

## Notlar

- Bu uygulama, kullanıcıları SQLite veritabanında saklar.
- Güncelleme kontrolü başlangıçta yapılır.
- Ciddi bir veri tabanı kullanmağınız önerilir. SQLite çok iyi bir seçim değildir

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır - [LICENSE](LICENSE) dosyasını inceleyin.
