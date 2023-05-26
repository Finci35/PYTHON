# 1- Girilen 2 sayıdan hangisi büyüktür?
# a = int(input("a: "))
# b = int(input("b: "))

# result = a > b

# print(f"a: {a} b: {b} den büyüktür : {result}")

# if a > b:
#     print(f"a: {a} b: {b} den büyüktür.")
# elif a < b:
#     print(f"a: {a} b: {b} den küçüktür.")
# else :
#     print(f"a: {a} ile b: {b} eşittir.")
    
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.

# vize1 = float(input("Birinci vize notunuzu girin: "))
# vize2 = float(input("İkinci vize notunuzu girin: "))
# final = float(input("Final notunuzu girin: "))

# result = ((vize1 + vize2) / 2 * 0.60) + (final * 0.40)

# if result >= 50:
#     print(f"Tebrikler **GEÇTİNİZ** // Ortalama notunuz: {result}")
# else :
#     print(f"Maalesef :( KALDINIZ :( || Ortalama notunuz: {result}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input("Bir sayı giriniz: "))

# if sayi % 2 == 0:
#     print(f"Girmiş olduğunuz sayı ({sayi}) çift bir sayıdır.")
# else :
#     print(f"Girmiş olduğunuz sayı ({sayi}) tek bir sayıdır.")


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

# sayi = int(input("Bir sayı giriniz: "))

# if sayi > 0:
#     print(f"Girmiş olduğunuz sayı ({sayi}) pozitif bir sayıdır.")
# else :
#     print(f"Girmiş olduğunuz sayı ({sayi}) negatif bir sayıdır.")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com    parola: abc123)

email = "email@sadikturan.com"
parola = "abc123"

print("Hesabınıza ulaşabilmek için mail adresinizi ve parolanızı giriniz.")
girilenEmail = (input("Mail adresiniz: ")).lower().strip() # büyük harfleri küçük yapar ve başta ve sondaki boşlukları kaldırır.
girilenParola = (input("Parolanız: ")).strip() # Başta ve sondaki boşlukları kaldırır.

if girilenEmail != email or girilenParola != parola:
    print("Email adresiniz ya da parolanız yanlış. Lütfen kontrol edip, tekrar deneyiniz.")
else :
    print("Bravo, hesabınıza giriş yaptınız.")


