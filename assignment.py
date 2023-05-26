# ***************** ATAMA OPERATÖRLERİ *******************

# x = 5
# y = 10
# z = 20

# Değişkenler yukarıdaki ya da aşağıdaki gibi tanımlanabilir.

x, y, z = 5, 13, 20

# x, y = y, x # x'e y'nin değeri, y'ye de x'in değeri atandı.

x += 5      # x = x + 5
x -= 5      # x = x - 5
x *= 5      # x = x * 5
x /= 5      # x = x / 5
x %= 5      # x = x % 5  modulo
y //= 5     # y = y // 5  y'yi 5'e böl, ondalıklı kısmı gösterme. Tam böleni y'ye ata.
y **= 5     # y = y ** 5  y üzeri 5 işlemini yapar. Sonucu y'ye atar.
y **= z     # y = y ** z  y üzeri z işlemini yapar ve sonucu y'ye atar.



values = 1, 2, 3  # tuple tipinde bir liste.
x, y, z = values # values'te tanımlı olan 1, 2, 3 verileri sırayla x, y ve z'ye atanır.

# values = 1, 2
# x, y, z = values # bu durumda hata mesajı verir. (ValueError: not enough values to unpack (expected 3, got 2))

values = 1, 2, 3, 4, 5
# x, y, z = values # bu durumda da hata mesajı verir. (ValueError: too many values to unpack (expected 3))
# Bu durumda z'yi * ile birlikte yazarsa z'ye [3, 4, 5] verileri atanır.
x, y, *z = values # Sonuç: 1 2 [3, 4, 5]


print(values)
print(type(values))



print(x, y, z)