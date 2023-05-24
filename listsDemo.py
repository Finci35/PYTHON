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


#

#

#


print(cars)
print(result)