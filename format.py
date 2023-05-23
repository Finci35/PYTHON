name = "Çınar"
surname = "Turan"
age = 40

print("My name is {} {}" .format(name, surname)) #Süslü parantezlerin yerine name ve surname değişkenleri gelecek.
# "name" sıfırıncı index ve "surname" ise birinci index olduğu için bu sırayla yazılır.
print("My name is {1} {0}" .format(name, surname)) # Burada surname'nin önce, name'nin ise sonra yazdırılmasını sağladık.
print("My name is {s} {n}" .format(n=name, s=surname)) # Burada index numarası yerine değişkenlere "n ve s" isimlerini verdik
                                                       # ve hangisinin önce yazdırılacağını belirledik.
print("My name is {} {} and I'm {} years old." .format(name, surname, age))


result = 200/9
print("The result is {r:1.7}" .format(r=result)) # Virgülün sol tarafına 1 boşluk bırakır ve sonucu toplam 7 basamaklı yapar.


# f string

print(f"My name is {name} {surname} and I'm {age} years old.")