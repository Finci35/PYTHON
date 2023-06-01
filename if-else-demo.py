# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontro ediniz.
#    Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# name = input('İsminizi giriniz: ')
# age = int(input('Yaşınızı giriniz: '))
# egitim = input('Eğitim durumunuzu giriniz (Yok - İlköğretim - Lise - Üniversite)')
# egitim = egitim.lower()

# if age >= 18:
#     if (egitim == 'lise') or (egitim == 'üniversite'):
#         print(f"{name} ehliyet alabilirsiniz.")
#     else :
#         print(f"{name} ehliyet alamazsınız. Ehliyet alabilmek için en az lise mezunu olmalısınız.")        
# else :
#     print(f"{name} ehliyet alamazsınız. Ehliyet alabilmek için en az 18 yaşında olmalısınız.")

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp,
# hesaplanan ortalamaya göre not aralığına karşıkı gelen not bilgisini yazdırınız.

# 0  - 24  => 0
# 25 - 44  => 1
# 45 - 54  => 2
# 55 - 69  => 3
# 70 - 84  => 4
# 85 - 100 => 5

# yazili1 = int(input('Birinci yazılı noutunuz: '))
# yazili2 = int(input('İkinci yazılı noutunuz: '))
# sozlu = int(input('Sözlü noutunuz: '))

# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if 0 <= ortalama <= 24:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 0')
# elif 25 <= ortalama <= 44:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 1')
# elif 45 <= ortalama <= 54:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 2')
# elif 55 <= ortalama <= 69:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 3')
# elif 70 <= ortalama <= 84:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 4')
# elif 85 <= ortalama <= 100:
#     print(f'Ortalamanız: {ortalama:2.4} --- Notunuz: 5')
# else :
#     print('Geçersiz bir veri girdiniz.')
    
    
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1. Bakım => 1. Yıl
# 2. Bakım => 2. Yıl
# 3. Bakım => 3. Yıl

# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı yapınız.
# *** datetime modülünü kullanılmalı.

import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9)')
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis # Çıktı: "600 days" şeklindedir. 
                            #Çıkarma işlemi yapabilmek için days ifadesinin kaldırılması gerekir.
days = fark.days # Bu işlem "days ifadesini kaldırır."

if days <= 365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2 :
    print("2. servis aralığı")
elif days > 365*2 and days <= 365*3 :
    print("3. servis aralığı")
else :
    print("Hatalı süre")
#

#

#

#

#

#

#

