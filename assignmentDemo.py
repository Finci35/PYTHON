x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplaının farkı nedir?
# a = int(input("Birinci sayı: "))
# b = int(input("İkinci sayı: "))

# result = a * b - (x + y + z)


# 2- y'nin x'e kalansız bölümünü hesaplayınız.

result = y // x

# 3- (x, y, z) toplamının mod 3'ü nedir?

result = (x + y + z) % 3 

# 4- y'nin x'inci kuvvetini hesaplayınız.

result = y ** x

# 5- x, *y, z = numbers işlemine göre Z'nin küpü kaçtır?
x, *y, z = numbers
# print(x, y, z)  # 1 [5, 7, 10] 6
                # x     y      z
result = z ** 3 # z = 6

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
print(x, y, z)

result = y[0] + y[1] + y[2]  # Sonuç: 22
print(result)
