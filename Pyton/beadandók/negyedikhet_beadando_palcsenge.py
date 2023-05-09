from math import *
import math


def elso_feladat():
    print("Első feladat: \n")
    print("50-ig számok egymás alatt: \n")
    
    for i in range(51) :
        print(i) 

    print("\n 182-től 212-ig számok egymás alá: \n")

    for i in range(182 ,  213) :
        print(i) 

    print("\n Páros számok egymás alá 100-tól 200-ig: \n") 

    for i in range(100 , 201 , 2) :
        print(i) 

    print("\n Páratlan számok visszafelé 89-től 57-ig: \n")

    for i in range(89 , 56 , -2) :
        print(i) 

    print("\n 1-től 20-ig számok és négyzetük: \n")

    for i in range(1 , 21) :
        print(i , i ** 2)

    print("\n 99-től csökkenő sorrendben levő 3-al osztható számok: \n")

    for i in range(99 , 1 , -3) :
        print(i)

    print("\n 101-től 50-ig csökkenő sorrendben 5-tel osztható számok: \n")

    for i in range(100 , 49 , -5) :
        print(i)

    print("\n Számok 1-től 1000-ig vesszővel elválasztva, ponttal a végén: \n")

    for i in range(1000) :
        print(i , end = ", ")
    print("1000.")

    print("\n 1000-től 1-ig 3-assával levő egész számok: \n")

    for i in range(1000 , 0 , -3) :
        print(i)

    print()

elso_feladat()

def masodik_feladat() :
    print("Második feladat: \n")
    print("100 db csillag: \n")

    for i in range(101) :
        print(end = "*")

    print("\n Bekért darabszámú bekért karakter: \n")

    darabszam = int(input("Adjon meg egy darabszámot: "))
    karakter = input("Adjon meg egy betűt: ")
    for i in range(darabszam) :
        print(end = karakter) 

    print("\n Bekért szöveg csillagozott keretben: \n")

    szoveg = input("Adjon meg egy szöveget: ")
    for i in range(len(szoveg) + 2) :
        print("*" , end = "")
    for i in range(1) :
        print("\n*" + szoveg + "*")
    for i in range(len(szoveg) + 2) :
        print("*" , end = "")

    print("\n 8*8-as sakktábla: \n")

    for i in range(4) :
        print(end = "* ")
    print()
    for i in range(4) :
        print(end = " *")
    print()
    for i in range(4) :
        print(end = "* ")
    print()
    for i in range(4) :
        print(end = " *")
    print()
    for i in range(4) :
        print(end = "* ")
    print()
    for i in range(4) :
        print(end = " *")
    print()
    for i in range(4) :
        print(end = "* ")
    print()
    for i in range(4) :
        print(end = " *")

    print()

masodik_feladat()

def harmadik_feladat() :
    print("Harmadik feladat: \n")

    szam1 = int(input("Adjon meg egy egész számot: "))
    szam2 = int(input("Adjon meg mégegy egész számot: "))
    lépésköz = int(input("Adjon meg harmadik egész számot: "))
    if szam1 < szam2 and lépésköz > 0 :
        for i in range(szam2 , szam1 - 1 , -lépésköz) :
            print(i)
    else :
        for i in range(szam1 , szam2 - 1 , lépésköz) :
            print(i)
    print()
    
harmadik_feladat()

def negyedik_feladat() :
    print("Negyedik feladat: \n")

    darabszam = int(input("Adjon meg egy darabszámot: "))
    if darabszam > 0 :
        for i in range(darabszam + 1) :
            print(2 ** i , end = "; ")
    else :
        print("Nincs negatív darab se 0 darab o.o")

    print()

negyedik_feladat()

def otodik_feladat() :
    print("Ötödik feladat: \n")

    darabszam = int(input("Adjon meg egy darabszámot: "))
    if darabszam > 0 :
        for i in range(darabszam + 1) :
            print(3 ** i)
    else :
        print("Nincs negatív darab se 0 darab o.o")

    print()

otodik_feladat()

def hatodik_feladat() :
    print("Hatodik feladat: \n")

    aSzam = int(input("Adjon meg egy egész számot: "))
    bSzam = int(input("Adjon meg egy másik egész számot: "))
    if aSzam < 0 and bSzam < 0 :
        print("Negatív számnak nincs négyzetgyöke o.o")
    else :
        for i in range(aSzam , bSzam):
            print(round(sqrt(i), 2))

    print()

hatodik_feladat()

def hetedik_feladat() :
    print("Hetedik feladat: \n")

    szam = int(input("Adjon meg egy egész számot: "))
    if szam <= 0 :
        print("Negatívnak és 0-ának nem számítható faktoriálisa o.o")
    else :
        fact = 1
        for i in range(1 , szam + 1) :
            fact = fact * i
        print("A(z) " + str(szam) + " faktoriálisa: " + str(fact))

    print()

hetedik_feladat()

def nyolcadik_feladat() :
    print("Nyolcadik feladat: \n")

    darabszam = int(input("Adjon meg egy darabszámot: "))
    if darabszam > 0 :
        for i in range(darabszam + 1) :
            print(2 ** i)
    else :
        print("Nincs negatív darab se 0 darab o.o")

    print()

nyolcadik_feladat()

def kilencedik_feladat() :
    print("Kilencedik feladat: \n")

    szam = int(input("Adjon meg egy pozitív egész számot: "))
    eredmeny = 0
    for i in range(1 , szam + 1 , 2) :
        eredmeny = eredmeny + i
    print(eredmeny)

    print()
   
kilencedik_feladat()

def tizedik_feladat() :
    print("Tizedik feladat: \n")
    eredmeny = 0
    szam = int(input("Adjon meg egy számot: "))
    for aktszam in range(szam , 0 , -1) :
        eredmeny = eredmeny + aktszam * (aktszam + 1)
    print(eredmeny)

    print()

tizedik_feladat()

def tizenegy_feladat() :
    print("Tizenegyedik feladat: \n")

    szam = int(input("Adjon meg egy természetes számot: "))
    for i in range(3 , szam + 1 , 3) :
        print(i)

    print()

tizenegy_feladat()

def tizenketto_feladat() :
    print("Tizenkettedik feladat: \n")
    
    szam1 = 0
    szam2 = 1
    
    darabszam = int(input("Adjon meg egy természetes számot: "))
    if darabszam == 1 :
        print(szam1)
    else :
        if darabszam == 0 :
            print("Érvénytelen adat, pozitív egész számot adjon meg.")
        else:
            print(szam1)
            print(szam2)
            for i in range(0 , darabszam - 2) :
                szam3 = szam1 + szam2
                szam1 = szam2
                szam2 = szam3
                print(szam3)

    print()
    
tizenketto_feladat()
