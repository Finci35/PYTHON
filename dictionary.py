# # key - value
# # 41 => kocaeli     34 => istanbul

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("istanbul")])

# # Yukarıdaki kodlar dictionary kullanmadan yapıldı, ama biraz daha zor.
# # Bunu dictionary kullanarak yapmak daha kolay. Aşağıdaki gibi

# ********** DICTIONARY *******************

# plakalar = {"kocaeli" : 41, "istanbul" : 34}
             #   key  : value 
                
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6 # plakalara ankara'yı ekler.
# plakalar["kocaeli"] = "new value" # kocaelinin plaka bilgisini "new value" olarak değiştirir.
# print(plakalar)

# Bir kullanıcıya çoklu giriş yapmak:
users = {
    "sadikturan": {
        "age" : 36,
        "roles" : ["user"],
        "email" : "sadik@gmail.com",
        "address" : "kocaeli",
        "phone" : "1231321"
    },
    "cinarturan": {
        "age" : 2,
        "roles" : ["admin", "user"],
        "email" : "cinar@gmail.com",
        "address" : "kocaeli",
        "phone" : "1231321"
    }
}

print(users["cinarturan"])
print(users["cinarturan"]["age"])
print(users["cinarturan"]["email"])
print(users["cinarturan"]["address"])

print(users["cinarturan"]["roles"])
print(users["cinarturan"]["roles"][0])