# name = '' # False
# while not name.strip(): # Bu ifade True'ya karşılık gelir. İsim girilmedikçe isim gir diye sormaya devam edecek.
# # Kullanıcı sadece boşluk karakteri girerse de kod çalışır. Bunu engellemek için
# # .strip() metodu kullanılır.    
#     name = input('İsminizi giriniz: ')

# print(f'Merhaba, {name}')

#############################################################################

# sayilar = [1, 3,5, 7, 9, 12, 19, 21]

# # 1- Sayilar listesini while ile ekrana yazdırın.

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
#    ekrana yazdırın.

# baslangıc = int(input('Başlangıç sayısını giriniz: '))
# j = int(input('Bitiş sayısını giriniz: '))

# i = baslangıc

# while i < j:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# numbers = []

# i = 0
# while i < 5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)    
    


# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#   ** Ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

urunSayisi = int(input('Kaç adet ürün girmek istiyorsunuz? '))

j = urunSayisi
i = 0

while i < j:
    name = input('Ürün ismi: ')
    price = input('Ürünün fiyatı: ')
    urunler.append({
        'name' : name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f"ürün adı: {urun['name']} --- urun fiyatı: {urun['price']}")

print(urunler)