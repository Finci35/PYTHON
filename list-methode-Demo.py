names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk ismini listenin sonuna ekleyiniz."
names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")

# 3- "Deniz ismini listeden siliniz."
# names.remove("Deniz")
#       ODER
# names.pop(-2)

# 4- "Deniz isminin indexi nedir?"
# index = names.index("Deniz")
# print(index)

# names.pop(index) # bu örnekte "Deniz"i listeden siler.

# 5- "Ali" listenin bir elemanı mıdır?
# result = "Ali" in names # True ya da False çıktısı verir.
# result = names.index("Ali") # 0 ya da pozitif bir değer verirse bu eleman listede vardır ve çıkan sonuç index numarasıdır.
#                             # listede yoksa hata mesajı verir.
# result = names.index("Fatih") # ValueError: 'Fatih' is not in list
# print(result)

# 6- Liste elemanlarını ters çevirin.
# names.reverse()
# ODER
# result = names[::-1]
# print(result)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"

str = str.split(",")
print(str)

# 10- years dizisinin en büyük ve en küçük elanı nedir?

max = max(years)
min = min(years)
print(max, min)

# 11- years dizisinde kaç tane 1998 değeri vardır?

result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.
# years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("marka1: ")
markalar.append(marka)

marka = input("marka2: ")
markalar.append(marka)

marka = input("marka3: ")
markalar.append(marka)

print(markalar)

#

#

print(names)
print(years)