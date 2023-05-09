import math


def elso_feladat() :
    
    hossz = int(input("A kert hossza: "))
    szel = int(input("Kert szélessége: "))

    megoldas = math.ceil((hossz * szel) / 5)

    print(f"{megoldas} zacskó mag lesz szükséges a kert bevetésére.")

elso_feladat()

def masodik_feladat() :
    
    szam = float(input("Adjon meg egy számot: "))
    ugh = szam / 2
    
    if ugh == int(ugh) and szam > 0 :
        print("Ez nem egy negatív páratlan szám")
    else :
        if szam < 0 and ugh == int(ugh) :
                print("Ez nem egy negatív páratlan szám")
        else :
            if szam < 0 and ugh == float(ugh) :
                print("Ez egy negatív páratlan szám")


masodik_feladat()

def harmadik_feladat() :

    szam2 = int(input("Adja meg a víz hőmérsékletét: "))

    if szam2 <= 0 :
        print("A víz halmazállapota szilárd. ")
    else :
        if szam2 > 0 and szam2 < 100 :
            print("A víz halmazállapota folyékony. ")
        else :
            if szam2 >= 100 :
                print("A víz halmazállapota gáz. ")

harmadik_feladat()

def negyedik_feladat() :

    darab = int(input("Adjon meg egy darabszámot: "))

    for i in range(1 , darab + 1) :
        i = i ** 2
        print(i , end = ";")

negyedik_feladat()

def otodik_feladat() :

    pozszam = int(input("Adjon meg egy pozitív egész számot: "))

    eredmeny = 0

    for aktszam in range(1 , pozszam + 1) :
        eredmeny = eredmeny + aktszam * (aktszam + 1)

    print(eredmeny)

otodik_feladat()