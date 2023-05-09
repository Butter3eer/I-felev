#Hátul while

import random

def husz_feladat():

    while True :
        szam = int(input("Kérek egy páros számot: "))
        if (szam%2==0) :
            print("A megadott szám páros!")
            break

husz_feladat()

def husz1_feladat() :

    while True :
        szam1 = int(input("Kérek egy pozitív számot: "))
        if(szam1 > 0) :
            print(szam1 % 5)
            break

husz1_feladat()

def husz2_feladat() :
    while True:
        nap = int(input("Kérek egy számot 1-7 között: "))
        if(1 <= nap <=7) :
            if(nap == 1) :
                print("hétfő")
            elif(nap == 2) :
                print("kedd")
            elif(nap == 3) :
                print("szerda")
            elif(nap == 4) :
                print("csütörtök")
            elif(nap == 5) :
                print("péntek")
            elif(nap == 6) :
                print("szombat")
            else:
                print("vasárnap")
            break
husz2_feladat()

def husz3_feladat() :

    while True :
        szam3 = int(input("Kérek egy negatív páratlan számot: "))
        if(szam3 > 0 or szam3 % 2 == 0) :
            print("Hiba!")
        else:
            break

husz3_feladat()

def husz4_feladat() :

    while True :
        szam4 = int(input("Kérek egy számot: "))
        if(szam4 % 3 == 0 and szam4 % 5 == 0) :
            print(szam4 / 3 , szam4 / 5 , sep = ' ')
            break

husz4_feladat()

def husz5_feladat() :

    while True :
        szam5 = int(input("Kérek egy számot: "))
        if(szam5 % 5 == 0) :
            break
        else:
            print(szam5 % 5)

husz5_feladat()

def husz6_feladat() :

    while True :
        aSzam = int(input("Kérek egy számot: "))
        bSzam = int(input("Kérek egy másik számot: "))

        if(aSzam == bSzam) :
            break
        elif(aSzam >  bSzam) :
            print("Első szám nagyobb mint a második")
        else :
            print("Második szám nagyobb mint az Első")

husz6_feladat()

def husz7_feladat() :

    while True :
        rSzam = random.randint(1 , 12)
        print(rSzam , rSzam % 3 , sep= ' ')
        ujsz = chr(ord(input("Új szám? (i / n) ")))
        if ujsz == 'n' :
            break

husz7_feladat()

def husz9_feladat() :

    gSzam = random.randint(1 , 50)

    while True :
        tipp = int(input("Tipp: "))
        if(tipp == gSzam) :
            break
        elif (tipp < gSzam) :
            print(" A gondolt szám nagyobb")
        else : 
            print("A gondolt szám kisebb")

husz9_feladat()