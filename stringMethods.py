message = " Hello There. My name is Fatih "

# message = message.upper() # message değişkeni içindeki tüm karakterleri büyük harf yapar.
# message = message.lower() # tüm karakterleri küçük harf yapar.
# message = message.title() # her kelimenin baş harfini büyük yapar.
# message = message.capitalize() # verilen string ifadenin sadece ilk harfini büyük yapar.
# message = message.strip() # verilen string ifadenin başında boşluk varsa onu yok eder.
#message = message.split() # verilen ifadenin her kelimesini aradaki boşluklara göre böler ve bir dizin oluşturur.
                          # ['Hello', 'There.', 'My', 'name', 'is', 'Fatih.']
# message = message.split(".") # noktalardan itibaren ayırır. ['Hello There', ' My name is Fatih']
# message = " ".join(message) # dizinin elemanlarını aralarına boşluk ekleyerek birleştirir.
                            # Hello There. My name is Fatih
# message = "*".join(message) # dizinin elemanlarını aralarına * ekleyerek birleştirir.
                            # Hello*There.*My*name*is*Fatih

#index = message.find("Fatih") # message değişkeninde Fatih kelimesini arar ve kaçıncı index numarasından itibaren başlağıdığı yazar.
                              # 24. Yani 24'ten itibaren Fatih kelimesi başlıyor.
                              # sonuç -1 olursa aranan kelime bu değişken içinde yok demektir.

# isFound = message.startswith("H") # message değişkeninin H harfi ile başlayıp başlamadığını kontrol eder. Büyük küçük harf duyarlıdır.
# isFound = message.endswith("h") # message değişkeninin h harfi ile bitip bitmediğini kontrol eder. Büyük küçük harf duyarlıdır.

# message = message.replace("Fatih", "Yavuz") # Fatih kelimesini bulur ve Yavuz ile değiştirir.
# message = message.replace(" ", "*") # boşlukları bulur ve yerlerine * ekler.
# message = message.replace("ü", "u")
#                  .replace("ö", "o")
#                  .replace("ç", "c")

# message = message.center(100) # 100 karakterlik bir alanda message değişkenindeki ifadeyi ortalar.
# message = message.center(50, "*") # 100 karakterlik bir alanda message değişkenindeki ifadeyi ortalar
                                  # ve sağ ve solundaki boşluklara * koyar.
                                  # **********Hello There. My name is Fatih***********


#print(isFound) 

print(message)

#print(message[0])