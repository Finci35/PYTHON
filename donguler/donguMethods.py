
# RANGE

# for item in range(5, 20, 3): # 5'ten başlar 3 arttırarak 20'ye kadar olan sayıları yazdırır.
#     print(item)

# print(list(range(5, 100, 10))) # liste oluşturur.

##########################################################################

# ENUMERATE

greeting = 'Hello'

index = 0

for letter in greeting:
    print(f"index: {index} letter: {letter}")
# oder    print(f"index: {index} letter: {greeting[index]}")
    index += 1

print("-------------------------------------------------------------")
    
# Yukarıdaki kod "enumerate" metodunu kullanarak aşağıdaki gibi yazılabilir:

greeting = 'Hello'

for index, letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")

print("-------------------------------------------------------------")


# ZIP

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3))) # [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1, list2, list3):
    print(item)     # (1, 'a', 100)
                    # (2, 'b', 200)
                    # (3, 'c', 300)
                    # (4, 'd', 400)
                    # (5, 'e', 500)

for a,b,c in zip(list1, list2, list3):
    print(a, b, c)      # 1 a 100
                        # 2 b 200
                        # 3 c 300
                        # 4 d 400
                        # 5 e 500
                        
