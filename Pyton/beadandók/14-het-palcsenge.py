def egy() :
    a = int(input("Adjon meg egy valós számot: "))
    b = int(input("Adjon meg egy másik valós számot: "))
    valasz = feladat(a , b)
    if valasz == 0 :
        print("A két szám egyenlő.")
    else :
        print(f"A {valasz} szám a nagyobbik. ")

def feladat(a , b) :
    if a > b :
        return a
    elif a < b :
        return b
    else :
        return 0

#egy()

def ketto() :
    ev = int(input("Adja meg az évet: "))
    honap = int(input("Adja meg a hónap számát: "))
    nap = int(input("Adja meg a napot: "))

    helyes = isHelyesDatumE(ev , honap, nap)
    if helyes == 1 :
        hosszDat = getHosszuDatum(ev , honap, nap)
        print(hosszDat)
    else :
        print("Helytelen dátum.")

def getHosszuDatum(ev , honap, nap):
    hosszDat = f"{ev}. "
    if honap == 1 :
        hosszDat = hosszDat + "Január "
    elif honap == 2 :
        hosszDat = hosszDat + "Február "
    elif honap == 3 :
        hosszDat = hosszDat + "Március "
    elif honap == 4 :
        hosszDat = hosszDat + "Április "
    elif honap == 5 :
        hosszDat = hosszDat + "Május "
    elif honap == 6 :
        hosszDat = hosszDat + "Június "
    elif honap == 7 :
        hosszDat = hosszDat + "Július "
    elif honap == 8 :
        hosszDat = hosszDat + "Augusztus "
    elif honap == 9 :
        hosszDat = hosszDat + "Szeptember "
    elif honap == 10 :
        hosszDat = hosszDat + "Október "
    elif honap == 11 :
        hosszDat = hosszDat + "November "
    else :
        hosszDat = hosszDat + "December "
    hosszDat = hosszDat + f"{nap}."
    return hosszDat

def isSzokoEv(ev) :
    if ev % 100 == 0 :
        return 1
    else :
        return 0

def isHelyesDatumE(ev , honap, nap) :
    if 1900 <= ev <= 2100 and 1 <= honap <= 12 :
        if honap == 1 or honap == 3 or honap == 5 or honap == 7 or honap == 8 or honap == 10 or honap == 11 :
            if 1 <= nap <= 31 :
                return 1
        elif honap == 2 :
            szoko = isSzokoEv(ev)
            if szoko == 1 :
                if 1 <= nap <= 29 :
                    return 1
            else :
                if 1 <= nap <= 28 :
                    return 1
        else :
            if 1 <= nap <= 30 :
                return 1
#ketto()

def harom() :
    a = int(input("Adjon meg egy számot: "))
    eredmeny = rajz(a)
    print(eredmeny)

def rajz(a):
    m = ""
    for i in range(a + 1) :
        sor = ""
        for j in range(a + 1):
            if i == 0 :
                sor = sor + f"{j}\t"
            elif j == 0 :
                sor = sor + f"{i}\t"
            else :
                sor = sor + f"{i * j}\t"
        m = m + sor + "\n"
    return m

#harom()

def negy() :
    fel1()
    fel2()
    fel3()

def fel1() :
    alap = int(input("Adjon meg egy számot: "))
    kitev = int(input("Adja meg a kitevőt: "))
    eredmeny = alap ** kitev
    print(eredmeny)

def fel2() :
    alap = int(input("Adjon meg egy számot: "))
    kitev = int(input("Adja meg a kitevőt: "))
    for i in range(1 , kitev + 1) :
        eredmeny = alap ** kitev
        print(f"{alap} ^ {kitev} = {eredmeny}")
    
def fel3() :
    alap = int(input("Adjon meg egy számot: "))
    kitev = int(input("Adja meg a kitevőt: "))
    if kitev != 0 :
        eredmeny = alap ** kitev
        print(eredmeny)
    elif kitev == 0 :
        print(1)

#negy()

from os import sep
import random


def ot() :
    op = int(input("1. nem\n2. Monogram\n3. Szül. idő\n4. Telefonszám\n5. Rendszám\n "))
    if op == 1 :
        nem()
    elif op == 2 :
        mono()
    elif op == 3 :
        szulId()
    elif op == 4 :
        tel()
    elif op == 5 :
        rendSz()
    else :
        ot()

def nem() :
    no = random.randint(0 , 2)
    if no == 1 :
        print("Férfi")
    elif no == 2 :
        print("Nő")
    else: 
        print("non-binary")

def mono() :
    vez = chr(random.randint(65 , 90))
    ker = chr(random.randint(65 , 90))
    print(f"{vez}. {ker}.")

def szulId() :
    evSz = random.randint(1900 , 2022)
    hon = random.randint(1 , 12)
    nap = random.randint(1 , 28)
    print(f"{evSz}. {hon}. {nap}.")

def tel() :
    mvv = random.randint(8 , 9)
    telsz = "+36 "
    resz1 = random.randint(10 , 99)
    resz2 = random.randint(100 , 999)
    resz3 = random.randint(100, 999)
    telsz = telsz + f"{resz1} {resz2} {resz3}"
    print(telsz)

def rendSz() :
    betu = ""
    szam = 0
    for i in range(3) :
        betu = betu + chr(random.randint(65 , 90))
    for i in range(3) :
        szam = szam * 10 + random.randint(0 , 9)
    print(f"{betu}-{str(szam)}")

#ot()

def hat() :
    szam = int(input("Adjon meg egy számot: "))
    eredmeny = 1
    for i in range(1 , szam + 1) :
        eredmeny *= i
    print(eredmeny)

    iras = "1"
    eredmeny = 1
    for i in range(2 , 6) :
        iras = iras + f" * {i}"
        eredmeny *= i
    print(f"{iras} = {eredmeny}")

hat()