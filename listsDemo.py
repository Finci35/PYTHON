# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2- Liste kaç elemanlıdır?
result = len(cars)

# 3- Listenin ilk ve son elemanı nedir?
result = cars[0], cars[-1]

# 4- Mazda değerini Toyota ile değiştirin.
cars[-1] = "Toyota" 
result = cars

# 5- Mercedes listenin bir elemanı mıdır?
result = "Mercedes" in cars # bulursa True, bulamazsa False

# 6- Listenin -2 indeksindeki değer nedir?
result = cars[-2]

# 7- Listenin ilk 3 elamanını alın.
result = cars[0:3]

# 8- Listenin son iki elemanı yarine "Toyota" ve "Renault" değerlerni ekleyin.
cars[-2:] = ["Toyota", "Renault"]
result = cars

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = cars +["Audi", "Nissan"] # Bu işlem cars dizinine eleman eklemez. Bunun için liste metetları kullanılır.
                                  # Sadece ekrana "Audi" ve "Nissan" elemanlarıyla yazdırır.

# 10- Listenin son elemanını silin.
del cars[-1]
result = cars

# 11- Liste elemanlarını tersten yazdırınız.
result = cars[::-1]

# 12- Aşağıdaki veriler bir liste içinde saklayınız.

        # studentA: Yiğit Bilgi 2010, (70, 60, 70)
        # studentB: Sena Turan  1999, (80, 80, 70)
        # studentC: Ahmet Turan 1998, (80, 70, 90)
        
studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet" "Turan", 1998, [80,70,90]]

students = [studentA, studentB, studentC]

result = students

# 13- Liste elemanlarını ekrana yazdırınız.
students = [studentA, studentB, studentC]
result = students

# Yiğit Bilgi 9 yaşında ve not ortalaması 66
result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {((studentA[3][0] + studentA[3][1] + studentA[3][2])/3):1.4}"

print(cars)
print(result)