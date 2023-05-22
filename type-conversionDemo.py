"""
Daire Alanı      : Pi * r²
Daire Çevresi    : 2 * Pi * r

* Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
Pi = 3.14

"""

r = float(input("Yarı Çapı Girin: ")) # str tipindeki veri girişini float tipine dönüştürdük.
pi = 3.14

DAlan = pi * r **2
DCevre = 2 * pi * r

print("Yarı Çapı " + str(r) + " olan dairenin alanı " + str(DAlan) + ", çevresi ise " + str(DCevre) + "dir.")
# float bir bilgi str bir birleştirmede kullanılamayacağı için burada
# tipi float olan r, DAlan ve DCevre değişkenlerini str'ye çevirdik.