# 11. OPERASI LOGIKA DAN BOOLEAN 
print("11. OPERASI LOGIKA DAN BOOLEAN")
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## NOT (Hasil akan selalu berkebalikan)
a = True
c = not a
print("# Not")
print("Data a =", a)
print("Data c =", c)
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## OR (Jika salah satu true, maka hasilnya true - Penambahan)
a = False
b = False
c = a or b
print("# Or")
print(a,"or",b,"=", c)

a = False
b = True
c = a or b
print(a,"or",b," =", c)

a = True
b = False
c = a or b
print(a," or",b,"=", c)

a = True
b = True
c = a or b
print(a," or",b," =", c)
print("")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## AND (Jika dua buah nilai true, maka hasil true - Perkalian
a = False
b = False
c = a and b
print("# And")
print(a,"and",b,"=", c)

a = False
b = True
c = a and b
print(a,"and",b," =", c)

a = True
b = False
c = a and b
print(a," and",b,"=", c)

a = True
b = True
c = a and b
print(a," and",b," =", c)
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## XOR (Akan  - Perkalian)
a = False
b = False
c = a ^ b
print("# XOR")
print(a,"XOR",b,"=", c)

a = False
b = True
c = a ^ b
print(a,"XOR",b," =", c)

a = True
b = False
c = a ^ b
print(a," XOR",b,"=", c)

a = True
b = True
c = a ^ b
print(a," XOR",b," =", c)
print("")
