'''
    ogrenciler = {
        "120": {
            "ad": "Ali",
            "soyad": "Yılmaz",
            "telefon": "532 000 00 01"
        },
        "125": {
            "ad": "Can",
            "soyad": "Korkmaz",
            "telefon": "532 000 00 02"
        },
        "128": {
            "ad": "Volkan",
            "soyad": "Yükselen",
            "telefon": "532 000 00 03"
        },
    }

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
   dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''

# **********VERSION 1 ******************

# ogrenciler = {}

# number = input("Öğrenci numaranız: ")
# name = input("İsminiz: ")
# surname = input("Soyisminiz: ")
# phone = input("Telefon numaranız: ")

# ogrenciler[number] = {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }


# **********VERSION 2 ******************

# ogrenciler = {}

# number = input("Öğrenci numaranız: ")
# name = input("İsminiz: ")
# surname = input("Soyisminiz: ")
# phone = input("Telefon numaranız: ")

# update metodunda birden fazla veri aynı anda eklenebilir.

# ogrenciler.update({
#     number : {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }
# })
# number = input("Öğrenci numaranız: ")
# name = input("İsminiz: ")
# surname = input("Soyisminiz: ")
# phone = input("Telefon numaranız: ")

# ogrenciler.update({
#     number : {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }
# })
# number = input("Öğrenci numaranız: ")
# name = input("İsminiz: ")
# surname = input("Soyisminiz: ")
# phone = input("Telefon numaranız: ")

# ogrenciler.update({
#     number : {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }
# })

# **********VERSION 2 ******************

ogrenciler = {}

sayi = input("Kaç öğrenci eklemek istiyorsunuz?")
sayi = int(sayi)
i = 0
while i < sayi:
    number = input('Öğrenci numaranız: ')
    name = input('İsminiz: ')
    surname = input('Soyisminiz: ')
    phone = input('Telefon numaranız: ')
    ogrenciler.update({
        number : {
            'ad' : name,
            'soyad' : surname,
            'telefon' : phone
        }
    })
    i +=1

# print(ogrenciler)    
print("*" * 50)


# 2'nci sorunun cevabı: *******************************

ogrNo = input("Öğrenci numarasını giriniz: ")

ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} , soyadı: {ogrenci['soyad']} ve telefonu: {ogrenci['telefon']}")