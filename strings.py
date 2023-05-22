name = "Fatih"
surname = "İnci"
age = 40

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."
length = len(greeting) # greeting değişkeninin kaç karakterden oluştuğunu sayar.


# print(greeting)

print(greeting[0]) # greeting değişkeninde tanımlı ifadenin sıfırıncı yani ilk karakterini yazdırır. (M)
print(greeting[3]) # greeting değişkeninde tanımlı ifadenin üçüncü indeksini yani dördürcü karakterini yazdırır. (n)
print(len(greeting)) # greeting değişkeninde kaç tane karakter olduğunu yazdırır.

print(greeting[length-1]) # greeting değişkeninin son karakterini yazdırır. (.)
print(greeting[-1])  # greeting değişkeninin son karakterini yazdırır. (.)
print(greeting[3:7]) # Üçüncü index numarasından yedinciye kadar yazdırır. (name)
print(greeting[3:])  # Üçüncü index numarasından başlar, sona kadar gider. 
print(greeting[:16]) # Baştan itibaren 16 index numaralı karaktere kadar gider. (My name is Fatih)
print(greeting[3:40:2]) # İndex numarası 3 olan karakterden 40'a kadar karakterleri 1 atlayarak yazar.
