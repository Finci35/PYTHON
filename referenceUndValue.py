# ******************* VALUE TYPES => string, int, float  *************************

x = 5
y = 25

x = y

y= 10

# value type'larda y x'e atandıktan sonra y'de yapılan bir değişiklik x'i değiştirmez.

print(x, y)  # Sonuç: 25 10

# ****************** REFERENCE TYPES ****************************

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b 

b[0] = "grape"

# reference type'larda b a'ya atandıktan sonra b'de yapılan değişiklik a'yı değiştirir.

print(a, b) # Sonuç: ['grape', 'banana'] ['grape', 'banana']