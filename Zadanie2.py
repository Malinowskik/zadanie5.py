# Zadanie 1
print("Zadanie1\n")
a = input("Wpisz dowolny komunikat: ")
aa = a.count("a")
print("W komunikacie literka a wsytąpiła: " + str(aa) + " razy")
print("\n")

# Zadanie 2
print("Zadanie2\n")
import sys as system
system.stdout.write("Wpisz  pierwszą liczbę całkowitą: ")
b = system.stdin.readline()
system.stdout.write("Wpisz  drugą liczbę całkowitą: ")
c = system.stdin.readline()
system.stdout.write("Wpisz  trzecią liczbę całkowitą: ")
d = system.stdin.readline()
e = int(b) ** int(c) + int(d)
print("Wynik: " + str(e))
print("\n")

# Zadanie 3
print("Zadanie3\n")
f = input("Wpisz liczbę całkowitą f: ")
g = input("Wpisz  drugą liczbę całkowitą g: ")
h = input("Wpisz  trzecią liczbę całkowitą h: ")
f = int(f)
g = int(g)
h = int(h)
if (f > g) & (f > h):
    print("Liczba f jest największa")
elif (g > f) & (g > h):
    print("Liczba g jest największa")
else:
    print("Liczba h jest największa")
print("\n")

# Zadanie 4
print("Zadanie4\n")
lista =[float(3.14), int(2), int(4), int(5), float(2.14)]
for i in range(5):
    print(lista[i] ** lista[i])
print("\n")

# Zadanie 5
print("Zadanie5\n")
lista2 = []
for j in range(10):
    k = input("Podaj liczbę całkowitą: ")
    if int(k) % 2 == 0:
        lista2.append(k)
print("Liczby parzyste:")
print(lista2)