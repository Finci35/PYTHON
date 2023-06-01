# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontro ediniz.

# sayi = float(input("Bir sayı giriniz: "))

# if sayi >= 0 and sayi <= 100:
#     print(f"Girdiğiniz sayı {sayi}, 0 ile 100 arasındadır.")
# elif sayi > 100:
#     print(f"Girdiğiniz sayı {sayi}, 100'den büyüktür.")
# else:
#     print(f"Girdiğiniz sayı {sayi}, negatif bir sayıdır.")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontro ediniz.

# sayi = float(input('Bir sayı giriniz: '))

# if (sayi >= 0):
#     if (sayi % 2 == 0):
#         print("Sayı pozitif bir çift sayıdır.")
#     else:
#         print("Sayı pozitif bir tek sayıdır.")
# else:
#     print("Sayı negatiftir.")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'email@fatih.com'
# password = 'parola123'

# username = input("Email adresinizi giriniz: ")
# parola = input("Parolanızı giriniz: ")

# if username == email:
#     if parola == password:
#         print("Tebrikler! Başarılı şekilde giriş yaptınız.")
#     else:
#         print("Parola hatalı. Lütfen tekrar deneyiniz.")
# else:
#     print("Kullanıcı adı hatalı. Lütfen ekrar deneyiniz.")
    
    
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = input("a sayısını giriniz: ")
# b = input("b sayısını giriniz: ")
# c = input("c sayısını giriniz: ")

# if (a>b) and (a>c):
#     print("a en büyük sayıdır.")
# elif (b>a) and (b>c):
#     print("b en büyük sayıdır.")
# elif (c>b) and (c>a):
#     print("c en büyük sayıdır.")
# else:
#     print("Yanlış bir veri girdiniz.")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp, ortalama hesaplayınız.

    # Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
    # a-) Ortalama 50 olsa bile final notu en az 50 olmaladır.
    # b-) Finalden 70 alındığında ortalamanın önemi olmasın.
    
    
vize1 = float(input('Birinci vize notunuzu giriniz: '))
vize2 = float(input('İkinci vize notunuzu giriniz: '))
final = float(input('Final notunuzu giriniz: '))

ortalama = (((vize1 + vize2) / 2) * 0.60) + (final * 0.40)

if ((ortalama >= 50) and (final >= 50)) or (final >= 70):
    print(f"Öğrenci {ortalama:2.4} ortalama ile dersten GEÇTİ.")
else:
    print(f"Öğrenci {ortalama:2.4} ortalama ile dersten KALDI.")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   
    # Formül: (Kilo / boy uzunluğunun karesi)
    
    # Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
    # 0-18.4      => Zayıf
    # 18.5-24.9   => Normal
    # 25.0-29.9   => Fazla Kilolu
    # 30.0-34.9   => Şiman (Obez)

# name = input("İsminiz: ")
# kilo = float(input("Kilonuz (kg): "))
# boy = int(input("Boyunuz (cm): "))

# index = kilo / ((boy/100) ** 2)

# zayıf = (index <= 18.4)
# normal = (index >= 18.5) and (index <= 24.9)
# kilolu = (index >= 25.0) and (index <= 29.9)
# obez = (index >= 30.0) and (index <= 34.9)

# print(f"{name} kilo indeksin: {index:2.4} ve kilo değerlendirmen zayıf {zayıf}")
# print(f"{name} kilo indeksin: {index:2.4} ve kilo değerlendirmen normal {normal}")
# print(f"{name} kilo indeksin: {index:2.4} ve kilo değerlendirmen kilolu {kilolu}")
# print(f"{name} kilo indeksin: {index:2.4} ve kilo değerlendirmen obez {obez}")

#

#

#

#

#

#

#

#

