list = [1, 2, 3]

tuple = (1, "iki", 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ["ali", "veli"]  # listenin eski elemanları yerine bunları atar.
tuple = ("damla", "ayşe") # tuple'ın eski elemanları yerine bunları atar.

list[0] = "ahmet" # Sıfırıncı index'e ahmet'i atar.
tuple[0] = "deniz" # TypeError: 'tuple' object does not support item assignment
# tuple'da herhangi bir eleman yerine başka bir eleman atanamıyor. Listeler ile arasındaki fark bu.
# Fakat tüm elemanların yerine yeni elemanlar atanabilir.
# tuple = ("fatma", "nazlı") # Bu kod "damla" ve "ayşe" siler, yerlerine "fatma" ve "nazlı"yı atar.




print(list)
print(tuple)

