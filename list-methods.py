numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers) # numbers değişkeninin en küçük elemanı.
val = max(numbers) # numbers değişkeninin en büyük elemanı.

val = max(letters) # letters değişkeninin en büyük elemanı.

val = numbers[3:6] # 3. index'ten 6.'ya kadar yazdırır. 3 dahil ama 6 dahil değil.
val = numbers[:3] # baştan 3. index'e kadar yazdırır. 3 dahil değil.
val = numbers[4:] # 4. indexten sona kadar yazdır. 4 dahil.

numbers[4] = 40 # 4. indexteki değeri 40 yapar.

# ***** LİSTEYE ELEMAN EKLEMEK *****
numbers.append(49) # en sona 49u ekler.
numbers.append(59) # en sona 59u ekler.

numbers.insert(3, 79) # 3. index'ten önce 79u ekler. Dolayısıyla yeni 3. index 79 olur.
numbers.insert(-1, 52) # son elemandan önce 52'yi ekler.
numbers.insert(len(numbers), 80) # en sona ekler.

# ***** LİSTEDEN ELEMAN SİLMEK *****
# numbers.pop() # son elemanı siler
# numbers.pop(-1) # bu da son elemanı siler.
# numbers.pop(1) # 1 index numaralı elemanı siler.

# numbers .remove(59) # 59 sayısını arar ve siler. Elemanları tek tek siler. 
#Örneğin listede 10 elemanı iki tane var. Tek hamlede ikisini birden silmez. Soldan başlayarak önce birinciyi, kodu tekrar çalıştırınca sonra ikinciyi siler.

# ***** LİSTENİN TÜM ELEMANLARINI SİLME ***********
# numbers.clear()


# ***** SIRALAMA *****
# numbers.sort() # küçükten büyüğe sıralar.
# numbers.reverse() # elemanların sıralamasını ters çevirir.

# letters.sort()
# letters.reverse()


# ***** ELEMAN SAYISINI BULMA *****
print(len(numbers)) # toplam eleman sayısını verir.
print(len(letters))

print(numbers.count(10)) # numbers içinde 10 elemanının kaç tane olduğunu sayar.
print(letters.count("a"))


print(val)
print(numbers)
print(letters)