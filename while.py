name = '' # False
while not name.strip(): # Bu ifade True'ya karşılık gelir. İsim girilmedikçe isim gir diye sormaya devam edecek.
# Kullanıcı sadece boşluk karakteri girerse de kod çalışır. Bunu engellemek için
# .strip() metodu kullanılır.    
    name = input('İsminizi giriniz: ')

print(f'Merhaba, {name}')

#############################################################################

sayilar = [1, 3,5, 7, 9, 12, 19, 21]

# 1- Sayilar listesini while ile ekrana yazdırın.



# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
#    ekrana yazdırın.

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#   ** Ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

