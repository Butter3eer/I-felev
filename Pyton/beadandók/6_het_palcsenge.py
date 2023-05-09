import random


def egy() :
    x = int(input("Adja meg a lista elemeinek számát: "))
    lista = []
    for i in range(x) :
        lista.append(input("Elem: "))
    print(*lista)
egy()

def ketto() :
    lista = []
    for i in range(7) :
        if random.randint(1,2) == 1 :
            lista.append("Igaz") 
        else :
            lista.append("Hamis")
    print(*lista)
ketto()

def harom() :
    lista = []
    for i in range(10) :
        lista.append(random.randint(5 , 25))
    print(*lista)
    lista.reverse()
    print(*lista)
    print(*lista[1 : 10 : 2])

    tipp = int(input("Adjon meg egy számot 1 és 10 között: "))

    while tipp < 10 :
        print(lista[tipp - 1])
        tipp = int(input("Adjon meg egy számot 2 és 10  között: "))
    print("Rossz érték.")

harom()

def negy() :
    lista1 = [1,2,3,4,5]
    lista2 = [1,2,3,4,5]
    lista3 = []
    for item1 , item2 in zip(lista1, lista2):
        lista3.append(item1 + item2)
    print(*lista3)
negy()

def ot() :
    lista = [1,2,3,4,5]
    lista.insert(1 , lista[-1])
    lista.pop(-1)
    print(lista)
ot()

def hat() :
    lista = []
    x = int(input("Adja meg a lista elemeinek számát: "))
    for i in range(x) :
        lista.append(input("Lista elem: "))
    print(*lista)
    lista.reverse()
    print(*lista)

hat()

def het() :
    lista = []
    osszeg = 0
    darab = int(input("Adja meg a lista elemeinek számát: "))
    for i in range(darab) :
        elem = int(input("Lista elem: "))
        osszeg += elem
        lista.append(elem)
    print(*lista)
    print(f"Ezen elemek összege: {osszeg}")
het()

def nyolc() :
    lista = []
    darab = int(input("Adja meg a lista elemeinek számát: "))
    for i in range(darab) :
        lista.append(int(input("Lista elem: ")))
    print(lista)
    for i in range(1, len(lista)-1, 2):
        lista[i] += lista[i + 1]
    print(lista)
nyolc()

def kilenc() :
    lista = []
    count = 0
    darab = int(input("Adja meg a lista hosszát: "))
    for i in range(darab) :
        lista.append(int(input("Lista elem: ")))
    for i in range(1, len(lista)) :
        if(lista[i] < 0 and lista[i - 1] > 0) :
            count += 1
    print(f"{count} db negatív szám van ebben a listában pozitív után. ")
kilenc()

def tiz() :
    lista = []
    darab = int(input("Adja meg a lista elemeinek számát: "))
    for i in range(darab) :
        elem = float(input("Lista elem: "))
        elem = round(elem, 2)
        lista.append(elem)
    print(lista)
tiz()