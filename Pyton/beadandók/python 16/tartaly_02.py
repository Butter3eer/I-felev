import random

def sugarak() :
    lista = []
    for index in range(8) :
        rand = round(random.uniform(25, 30), 2)
        lista.append(rand)
    return lista

lista = sugarak()

def urtartalom(lista) :
    eredmeny = []
    for item in lista :
        V = round(((item*item) * 3.14) * 20, 1)
        eredmeny.append(V)

    print("A tartályok űrtartalma: ")
    db = 1
    for item in eredmeny :
        print(f"\t{db}.: {item} l")
        db += 1

urtartalom(lista)