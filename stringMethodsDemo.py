website = "http://www.sadikturan.com"
course = "Python kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = " Hello World ".strip()
result = " Hello World ".lstrip() # soldaki boşlukları siler.
result = " Hello World ".rstrip() # sağdaki boşlukları siler.

result = website.lstrip("htp:/") # website değişkeninde tanımlı ifadenin
                        # solundaki (parantez içinde belirtilen) karakterleri siler.

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = "www.sadikturan.com".strip("w.com")

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower() # küçük
result = course.upper() # büyük
result = course.title() # baş harfleri büyük

# 4- "website" içinde kaç tane a karakteri vardır? (count("a"))
result = website.count("a")
result = website.count("www")
result = website.count("www", 0, 10) # sıfırıncı ile onuncu index arasında kaç tane var?

# 5- "website" www ile başlayıp com ile bitiyor mu?
result = website.startswith("www")
result = website.endswith("com")

# 6- "website" içinde ".com" ifadesi var mı?
result = website.find(".com")
result = website.find(".com", 0, 10) # sıfırıncı ile onuncu index arasında var mı?

result = course.find("Python")
result = course.rfind("Python") #aramaya sağdan başlar.

result = website.index("com")
result = website.rindex("com") #aramaya sağdan başlar.
# result = website.index("comm") # olmaya bir kelime aratılınca hata mesajı verir.
                               # ValueError: substring not found
# FIND ile INDEX arasındaki FARK:
# FIND bulamazsa sonuç olarak -1 verir.
# INDEX bulamazsa sonuç olarak hata mesajı verir. (ValueError: substring not found)

# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha() # course değişkeninin içindeki ifadelerin alfabetik olup olmadğını sorgular.
                          # sayılar da olduğu için sonuç False'dur.
result = course.isdigit() # course değişkeninin içindeki ifadelerin sayısal olup olmadğını sorgular.
                          # harfler de olduğu için sonuç False'dur.

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "Contents".center(50, "*")
result = "Contents".ljust(50, "*") # sola yaslar ve sağa doğru yıldız ekler.
result = "Contents".rjust(50, "*") # sağa yaslar ve sola doğru yıldız ekler.

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
result = course.replace(" ", "-")
result = course.replace(" ", "-", 5) # ilk 5 boşluğu değiştir.
result = course.replace(" ", "") # bütün boşlukları siler.

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
result = "Hello World".replace("World", "There")

# 11- "course" karakter dizisini boşluk karakterlerinden ayırın.
result = course.split()


print(result)