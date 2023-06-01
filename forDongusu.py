numbers = [1, 2, 3, 4, 5]

for num in numbers:
   # print(num) # 1
               # 2
               # 3
               # 4
               # 5
    print('Fatih') # Fatih
                   # Fatih
                   # Fatih
                   # Fatih
                   # Fatih

# LİSTELER

names = ['çınar', 'sadık', 'sena']

for name in names:
    print(f'my name is {name}')  # my name is çınar
                                 # my name is sadık
                                 # my name is sena
                                 
name = 'Fatih'

for n in name:
    print(n)    # F
                # a
                # t
                # i
                # h    

tuple = [(1, 2), (1, 3), (3, 5), (5, 7)]

# TUPLE LİSTELERİ

for t in tuple:
    print(t)    # (1, 2)
                # (1, 3)
                # (3, 5)
                # (5, 7)

for a,b in tuple:
    print(a)    # 1
                # 1
                # 3
                # 5
for a, b in tuple:
    print(a, b) # 1 2
                # 1 3
                # 3 5
                # 5 7

# DICTIONARY

d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item) # k1 # Bu şekil de sadece key bilgilerini alır.
                # k2
                # k3
for item in d.items():
    print(item) # ('k1', 1) # Bu şekilde eleman gruplarına ulaşılabilir.
                # ('k2', 2)
                # ('k3', 3)
for key, value in d.items():
    print(key, value)   # k1 1  # Hem key hem de value bilgilerine ulaşılır.
                        # k2 2
                        # k3 3
for key, value in d.items():
    print(key)  # k1    # Sadece key bilgilerine ulaşılır.
                # k2
                # k3