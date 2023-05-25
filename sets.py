fruits = { 'orange', 'apple', 'banana' }


# print(fruits[0]) # indekslenemez.

for x in fruits:
    print(x)


# *********** SET'E ELEMAN EKLEMEK **********************

fruits.add('cherry') # tek seferde sadece bir eleman eklenebilir.
fruits.update(['mango', 'grape', 'apple'])
# Birden fazla eleman eklemek için update metodu kullanılır.
# Eğer zaten listede bulunan bir eleman tekrar eklenmek istenirse, bu ignore edilir. Eklenmez.

# *********** SET'TEN ELEMAN SİLMEK **********************

fruits.remove('mango')
fruits.discard('apple')
fruits.pop() # indexlenebilir listelerde son elemanı siliyordu. 
# Fakat setler gibi indexlenemeyen listelerde hangi elemanı sileceği belli olmaz :)

fruits.clear() # tüm elemanları siler.

print(fruits)

# myList = [1, 2, 5, 4, 4, 2, 1]
# print(myList)
# print(set(myList)) # set kullanılırsa tekrar eden elemanlar yazdırılmaz.

