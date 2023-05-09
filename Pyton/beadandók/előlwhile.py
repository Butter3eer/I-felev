#Elől while
import random


def elso_feladat() :

    print(random.randint(0 , 10))
    print(random.randint(10 , 15))
    print(random.randint(0 , 100))
    print(random.randint(-100 , 100))

    for i in range(0 , 10) :
        rand = random.randint(0 , 1)
        print(end = f"{rand} ")
    
    print()

    for i in range(0 , 4) :
        print(random.randint(-10 , 30))
        

elso_feladat()


def masodik_feladat() :

    szam = random.randint(0 , 1)
    tipp = int(input("Tippelje meg hogy fej vagy írás! Fej = 0 , írás = 1 : "))

    while tipp!= szam :
        szam = random.randint(0 , 1)
        tipp = int(input("Majdnem talált! Új tipp: "))
    print("Gratu! Talált!")

masodik_feladat()

def negyedik_feladat() :

    szam1 = int(input("Adjon meg egy számot: "))
    eredmeny = szam1

    while szam1 != 0 :
        szam1 = int(input("Új szám: "))
        eredmeny = eredmeny * szam1
        print(eredmeny)
    print("A szám 0 volt!")

negyedik_feladat()

def otodik_feladat() :

    szo = "alma"
    print(szo)
    szo2 = input("Másik szó: ")
   
    while (szo2 !=" ") :
        szo = szo + " " + szo2
        print(szo)
        szo2 = input("Másik szó: ")

otodik_feladat()

def hatodik_feladat() :

    darabszam = int(input("Darabszám: "))
    karakter = input("Karakter: ")
    string = ""
    while(darabszam != 0 ) :
        string = string + karakter
        darabszam = darabszam - 1
    print(string)

hatodik_feladat()

def hetedik_feladat() :
    aSzam = int(input("Adjon meg egy számot: "))
    bSzam = int(input("Adjon meg egy másik számot: "))
    lepeskoz = int(input("Lépésköz: "))
    string = ""

    if ( aSzam > bSzam) :
        lepeskoz = - lepeskoz


    string += str(aSzam)
    while aSzam != bSzam :
        aSzam += lepeskoz
        string = string + str(aSzam)

    print(string)

hetedik_feladat()
        
def nyolcadik_feladat() :

    szam = 1

    while(szam < 1000) :
        if(szam % 3 == 0) :
            if(szam % 5 == 0) :
                print(szam)
        szam += 1

nyolcadik_feladat()

def kilencedik_feladat() :
    penz = int(input("Pénzösszeg: "))
    counter = 0

    while(penz >= 200) :
        penz -= 200
        counter += 1
    print(f"{counter} db 200ft")
    counter=0
    while(penz >= 100) :
        penz -= 100
        counter += 1
    print(f"{counter} db 100ft")
    counter=0
    while(penz >= 50) :
        penz -= 50
        counter += 1
    print(f"{counter} db 50ft")
    counter=0
    while(penz >= 20) :
        penz -= 20
        counter += 1
    print(f"{counter} db 20ft")
    counter=0
    while(penz >= 10) :
        penz -= 10
        counter += 1
    print(f"{counter} db 10ft")
    counter=0
    while(penz >= 5) :
        penz -= 5
        counter += 1
    if penz > 0 :
        c += 1
    print(f"{counter} db 5ft")

kilencedik_feladat()