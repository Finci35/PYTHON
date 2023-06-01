# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y) #true  Burada değer karşılaştırması yapılır.
print(x == z) #True  Burada da değer karşılaştırması yapıldığı için sonuç True çıkar.

# is ile referans tipindeki verilerin adres karışlaştırılması yapılır.
print(x is y) # True  Adres aynı.
print(x is z) # False    Değer aynı olsada Adres farklı.

print("---------------------------------------------")

a = [1, 2, 3]
b = [2, 4]

del a[2] # a = [1, 2]
b[1] = 1 # b = [2, 1] 
b.reverse() # b = [1, 2]

print(a == b) # True
print(a is b) # False       a ile b'nin adresleri aynı mı? 
print(a is not b) # True    a ile b'nin adresleri aynı değil mi? 

print('-------------------------------------------------------------')


# Membership Operator: in

x = ['apple', 'banana']
print('banana' in x)

name = 'Çınar'
print('a' in name)  # True
print('a' not in name) # False
