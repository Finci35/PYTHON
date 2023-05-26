# ************* MANTIKSAL OPERATÖRLER ****************

x = 5

result = 5 < x < 10

# and

# True, True => True
# True, False => False

result = (x > 5) and (x < 10)

hak = 3
devam = 'e'

result = (hak > 0) and (devam == 'e')

# or

# True, True => True
# True, False => True
# False, False => False
result = (x > 0) or (x % 2 == 0)

# not

result = not(x > 0) # Sonucu tam tersine çevirir. Sonuç True ise not kullanınca False olur.

print(result)