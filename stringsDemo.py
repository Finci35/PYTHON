website = "http://www.sadikturan.com"
course = "Python kursu: Baştan Sona Python Programlama rehberiniz (40 saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır?

print(len(course))

# 2- "website" içinden www karakterlerini alın.

print(website[7:10])

# 3- "website" içinden com karakterlerini alın.

print (website[-3:])
print(website[22:25])

length = len(website)
result = website[length-3:length]
print(result)

# 4- "course" içinden ilk 15 ve son 15 karakterleri alın.

print(course[:15], course[-15:])

# 5- "course" içindeki karakterleri tersten yazdırın.

print(course[::-1]) # iki tane ":" işareti course içindeki tüm karakterleri alır.
                    # "-1" ise bu karakterleri sondan başa doğru yazdırır.
                    

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

print("Benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve Mesleğim " + job + ".")
print("Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name, surname, age, job))
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7- "Hello world" ifadesindeki w harfini "W" ile değiştirin.

s = "Hello world"
s = s[0:6] + "W" + s[-4:] # String ifade içindeki bir karakteri direk değiştiremediğimizi için bu şekilde bir kod yazdık.

print(s)


# 8- "abc" ifadesini yan yana 3 defa yazdırın.

print("abc " * 3)
