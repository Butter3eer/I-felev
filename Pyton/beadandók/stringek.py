import random


def elso() :
    szo = input("Adjon meg egy szót: ")
    for i in szo :
        print(i)
#elso()

"""
def elso() :
    email = input("Adjon meg egy email címet: ")
    if " " in email :
        print("Nem lehet benne szünet. ")
    elif '@' not in email :
        print("Nincs benne @. ")
    elif email[0] == '.' :
        print("Ponttal nem kezdődhet. ")
    elif "." not in email :
        print("Nincs benne pont. ")
    else :
        print(*email)
masodik()
"""
def elso() :
    angszo = input("Adjon meg egy angol szót: ")
    darab = 0
    maganhang = "aáeéoóöőuúüűií"
    for betu in angszo :
        if betu in maganhang :
            darab += 1
    print(f"Ebben a szóban {darab} db magánhangzó van. ")
#elso()

def elso() :
    szam = input("Adjon meg egy számot: ")
    eredmeny = 0
    if int(szam) < 10 :
        print("Legalább 2 jegyű legyen a szám. ")
    else :
        for jegy in szam :
            eredmeny += int(jegy)
        print(eredmeny)
#elso()

def elso() :
    lista = []
    eredmeny = 0
    darab = 0
    for i in range(10) :
        lista.append(random.randint(-100 , 100))
    for szam in lista :
        if szam % 2 == 0 :
            darab += 1
    for szam in lista :
        eredmeny += szam
    print(*lista)
    print(f"A lista elemeinek összege: {eredmeny}")
    print(f"A listában {darab} db páros szám van. ")
#elso()

def elso() :
    lista = []
    darab = 0
    magdarab = 0
    for i in range(5) :
        lista.append(input("Lista szó: "))
    resz = input("Adjon meg egy szó részletet: ")
    for index in range(len(lista)) :
        if lista[index].find(resz) == 0 :
            darab += 1
    for i in range(len(lista)) :
        maganhang = "aáeéoóöőuúüűií"
        for index2 in range(len(maganhang)) :
            if maganhang[index2] in lista[i] :
                magdarab += 1
    
    lista.sort()
    print(f"Ezzel a részlettel {darab} db szó kezdődött. ")
    print(lista[-1] , " a leghosszabb begépelt szó. ")
    print(f"A lista szavaiban {magdarab} db magánhangzó van. ")

elso()