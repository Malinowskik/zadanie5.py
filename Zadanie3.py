# Zad 1
print("Zadanie 1")
a = [1 - x for x in range(1, 11)]
print(a)
b = [4**i for i in range(8)]
print(b)
c = [x for x in b if x % 2 == 0]
print(c)
print('\n')

# Zad 2
print("Zadanie 2")
from random import seed
from random import randint
seed(1)
for i in range(10):
    lista1 = randint(0,10)
    lista2 = [i for i in range(lista1) if i % 2 == 0]
print(lista2)
print('\n')

# Zad 3
print("Zadanie 3")
slownik = {"ziemniaki": "kg", "jajka":  "szt", "mleko": "litry"}
wyszukane = [key for key, value in slownik.items() if value.count("szt")]
print(wyszukane)
print('\n')

# Zad 4
print("Zadanie 4")
'''
d = input ("Podaj długość boku a: ")
e = input("Podaj długość boku b: ")
f = input("Podaj długość boku c: ")
# zakładam że użytkownik podaje odpowiednie długości
if (float(d) <= 0) | (float(e) <= 0) | (float(f) <= 0):
    print("bląd, długośc nie może być ujemna lub równa   0")
elif (float(d)**2 + float(e)**2 == float(f)**2) | (float(e)**2 + float(f)**2 == float(d)**2) | (float(d)**2 + float(f)**2 == float(e)**2):
    print("trójkąt prostokątny")
else: print("to nie jest trójkąt prostokątny")
print("\n")
'''
# Zad 5
print("Zadanie 5")
import math
import random
def p_trapez(a = random.randint(1,10), b = random.randint(5,15), c = random.randint(10,20)):
    print("Pole trapezu wynosi: ")
    return ( a + b * c /2)
print(p_trapez())
print("\n")

# Zad 6
print("Zadanie 6")
def ciag(g = 1, h = 4, ile = 10):
    k = []
    l = 0
    if ile <= 0:
        print("błą! ile nie może być mniejsze lub równe zeru")
        return 0
    elif ile == 1:
        return g*h
    else:
        while l != ile:
            g *= h
            k.append(g)
            l += 1
        return k
print(ciag())
print("\n")

# Zad 7
print("Zadanie 7")
def ciag1(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        wynik = liczby[0]
        for i in liczby:
            wynik *= i
        return wynik
print(ciag1())
print(ciag1(1))
print((ciag1(1, 2, 3, 4, 5)))
print((ciag1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# Zad 8
print("Zadanie 8")
def zakupy(** produkt):
    print("Liczba produktów:")
    print(len(produkt))
    print("Laczna warotsc:")
    print(sum(produkt.values()))
zakupy(chleb = 3, monster = 2.80, jajka = 5.34, dzienwolny = 120)
print("\n")

# Zad 9
import moduły.aryt
import moduły.geo
print("Zadanie 9")
print("przykładowuy n-ty wyraz ciągu arytmetycznego")
print(moduły.aryt.nx(3,9,3))
print("suma n wyrazów ciągu")
print((moduły.aryt.suma_n(5,4,3)))
print("\n")
print("przykładowuy n-ty wyraz ciągu geometrycznego")
print(moduły.geo.nx(3,9,3))
print("suma n wyrazów ciągu")
print((moduły.geo.suma_n(5,4,3)))
print("\n")

# Zad 10
print("Zadanie 10")
# plik stworzony
print("\n")

# Zad 11
print("Zadanie 11")
plik = open("przedział.py","r+")
wiersze = plik.readlines()
print("\n")
print(wiersze)