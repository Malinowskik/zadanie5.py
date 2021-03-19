# Zadanie 1

# Integer
a = int(2.1)
aa = int(3.7)
print(a, aa)

# Float
b = float(420.6)
bb = float(6.66)
print(b, bb)

# String
c = 'String'
cc = 'nanana'
print(c, cc)

# Complex
d = 2 + 2j
dd = 33 + 3j
print("{} + {} = {}".format(d, dd, d+dd))

# Zadanie 2
a += 2
b -= 4
aa *= 4
bb /= 3.33
e = 3
e **= 2
ee = 6
ee %= 5

print(a, b, aa, bb, e, ee)

# Zadanie 3
# a)
import math
print((math.e ** 10))
# b)
print(math.log(5 + (math.sin(8))**2)**1.6)
# c)
x = range(3, 55)
for n in x:
  print(n)
# d)
y = range(4, 80)
for n in y:
  print(n)

# Zadanie 4
imie = 'KRZYSZTOF'
naziwsko = 'MALINOWSKI'

print(imie.capitalize() + ' ' + naziwsko.capitalize())

# Zadanie 5
txt = " La la la la la la la na na na na na La la na na la la la la la na na na na na La la la la la la la na na na na na La la na na la la la la la na na na na na Hush dont speak When you spit your venom keep it shut I hate it"
tx = txt.count("la")
print(tx)

# Zadanie 6
txt2 = "Jajko Na Twardo"
print(txt2[1] + ' ' + txt2[14])

# Zadanie 7
tx2 = txt2.split()
print(tx2)

# Zadanie 8
string8 = 'string'
float8 = float(3.14)
hex8 = hex(255)
print(string8)
print(float(float8))
print(hex8)

# Zadanie 9
lista = ['snooker', 'siatkówka', 'football', 'poker']
lista.reverse()
lista.append('nożna')
lista.append('narciarstwo')
print(lista)

# Zadanie 10
slownik = {'wyd.': 'wydanie', 't.': 'tom', 'nr': 'numer', 'red.': 'redakcja', 'wydawn.': 'wydawnictwo', 'tłum.': 'tumaczenie',}
print(slownik.keys())
print(slownik.values())