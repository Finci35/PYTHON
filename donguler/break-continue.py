name = 'Sadık Turan'

for letter in name:
    if letter == 'a':
#        continue # Döngü a harfine gelince, a'yı yazdırmadan diğer harfe geçer.
         break # Döngü a harfine gelince, döngüyü bitirir, devam etmez.
    print(letter)
    
######################################

x = 0

while x < 5:
    if x == 2:
        break  # işlem durdurulur. Çıktı da sadece 0 ve 1'i gösterir.
    print(x)
    x += 1


y = 1

# while y < 5:
#     if y == 2:
#         continue  # Bu dizilimde, continueden sonra gelen kod blokları işletilmediğinden
#                   # dolayı y 2'de takılı kalacak ve sonuç gösterilmeyecek.
#                   # Bu sebeple "y += 1" kodu if'in üstüne taşınmalı.
                    # Bu durum başlangıç değeri atlanır. Örneğin, başlangıç değeri 1 ise, 1 yazdırılmaz
#     print(y)
#     y += 1

# Yukarıdaki kod aşağıdaki gibi yazılmalı:

while y < 5:
    y += 1  # Bu durum başlangıç değeri atlanır. Örneğin, başlangıç değeri 1 ise, 1 yazdırılmaz.
    if y == 2:
        continue # Döngü 2'ye gelince, 2yi atlar 3'ten devam eder.
    print(y)
    

# 1 - 100 e kadar tek sayıların toplamı:

toplam = 0

i = 0

while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    toplam += i
print(toplam)