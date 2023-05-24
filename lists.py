# my_list = [1, 2, 3]
# my_list = ["bir", 2, True, 5.6]
# print(my_list)

list1 = ["one", "two", "there"]
list2 = ["four", "five", "six"]

numbers = list1 + list2
print(numbers)
print(len(numbers))
print(numbers[2]) # 2 index numaralı eleman (yani üçüncü eleman) yazdırılır.


userA = ["Sadık", 36]
userB = ["Çınar", 2]

# users = userA + userB # userA ve userB bilgilerini yanyana yazdırır. ['Sadık', 36, 'Çınar', 2]

# Fakat liste içinde liste yapılmak istenirse şöyle yapılmalı:
users = [userA, userB] # [['Sadık', 36], ['Çınar', 2]]
                       #      0     1        0     1
                       #    0. index   ,   1. index

print(users[0]) # ['Sadık', 36]
print(users[1]) # ['Çınar', 2]
print(users[0][0]) # Sadık
print(users[0][1]) # 36
print(users[1][0]) # Çınar
print(users[1][1]) # 2