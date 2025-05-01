
Proje Adı: ModHub

Ana Konu: Destek paneli kullanıcıların yaşadığı sorunu hızlı bir şekilde çözmek ve onlara yardımcı olmak.

Sitenin Konusu: Oyunlar için mod sayfası, kullanıcıların yüklemek istedikleri oyun modlarını bulup indirmelerine olanak tanır.

---

Mevcut Durum:

1. Ana Sayfa:
   - Gri ve turuncu tasarım kullanılarak oluşturulmuş.
   - Sağ altta deneme olarak açılıp kapanabilen bir müzik eklenmiştir.

2. Navbar:
   - Sol kısmında:
     - Sitenin ismi,
     - Ana Sayfa tuşu ve
     - Yöneticiler için giriş bulunmaktadır.
   - Sağ kısmında:
     - Giriş yapmak için bir tuş,
     - Kayıt olmak için bir tuş ve
     - Destek paneline erişim sağlayan bir tuş yer almaktadır.

3. Body:
   - "ModHub'a hoş geldiniz" yazısı ve altında basit bir açıklama yer alır.
   - Altında, 2 adet Kayıt Ol ve Giriş Yap tuşları bulunur.
   - Kullanıcılar, Oyun içeriklerine erişebilecekleri kart tarzında oyunlar ile karşılaşırlar. Her kartın giriş tuşuna basılarak mod sayfasına yönlendirilirler.

4. Mod Sayfası:
   - Mod sayfasında filtreleme yapılabilen bir alan bulunur.
   - Modlar, kart tasarımına sahip olup, beğenme sayısı, indirme sayısı ve yapımcının ismi yer alır.
   - Mod sayfasına girildiğinde, yüklenme tarihi, mod sürümü, mod kategorisi, mod ismi, mod görseli, indirme tuşu, favori tuşu ve yorum tuşu görünür.
   - Ayrıca açıklamalar, kurulum talimatları ve gereksinimler gibi bilgiler de yer alır.
   - Footer kısmında yorumlar bulunabilir.

5. Proje Yapısı:

   2_Hafta
   ├── static/
   │   ├── css/
   │   │   ├── base.css
   │   │   ├── destek.css
   │   │   └── mod_sayfa_1.css
   │   ├── images/
   │   │   ├── bannerlord.jpeg
   │   │   ├── fallout4.jpg
   │   │   ├── floris.png
   │   │   ├── Immersive_Armors.png
   │   │   ├── Minimal_Hud.png
   │   │   ├── Mod_Eklenecek.png
   │   │   ├── Realm.png
   │   │   ├── Skyrim_Anniversary_Edition.jpeg
   │   │   ├── Skyrim_Resim.png
   │   │   └── Warband.jpeg
   │   └── music/
   │       └── Adaption.mp3
   ├── templates/
   │   ├── admin.html
   │   ├── bannerlordmods.html
   │   ├── base.html
   │   ├── destek.html
   │   ├── fallout4mods.html
   │   ├── index.html
   │   ├── login.html
   │   ├── mod_sayfa_1.html
   │   ├── mod_sayfa_2.html
   │   ├── mod_sayfa_3.html
   │   ├── mod_sayfa_4.html
   │   ├── register.html
   │   ├── skyrimmods.html
   │   └── warbandmods.html
   └── app.py   

6. Şu Anda:
   - Platformda 4 oyun için sadece 1 mod eklenmiştir.

---

Gelecek Planlama:

7. Destek Paneli:
   - Destek paneli, ayrı bir sayfa yerine sağ altta açılabilir bir pencere tasarımında olacak.
   - Kullanıcılar bu panel üzerinden sorunlarını bildirebilecek ve cevap alabilecek.
   - Her giriş yapan üye, kendi profilini görüntüleyebilecek, mod yükleyebilecek, profillerini düzenleyebilecek, favori modlarını görüntüleyebilecek ve açtıkları destek panellerini ve yaptıkları yorumları inceleyebilecek.

---

Eklenecek Modlar ve Mevcut Durum:
- Şu an için platformda sadece 1 mod eklenmiş olsa da, 4 farklı oyun için modlar eklenmeye devam edilecektir. Bu, sitenizin büyüme potansiyelini göstermektedir.

---
