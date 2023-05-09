import random


def elso() :
    
    old = int(input("Adja meg a háromszög oldalát: "))
    mag = int(input("Adja meg a háromszög megadott oldalához tartozó magasságot: "))
    ter = (old * mag) / 2
    print(f"A háromszög területe {ter}.")

elso()

def masodik():
    a = int(input("A háromszög a oldala: "))
    b = int(input("B háromszög b oldala: "))
    c = int(input("C háromszög c oldala: "))
    if (a + b > c) and (b + c > a) :
        print("Ez egy háromszög.")
    else :
        print("Ez NEM egy háromszög. ")
masodik()

def harmadik() :
    a = int(input("Adja meg a háromszög a oldalát: "))
    b = int(input("Adja meg a háromaszög b oldalát: "))
    c = int(input("Adja meg a háromaszög c oldalát: "))

    if a == b or b == c or c == a :
        print("Ez egy egyenlő szárú háromszög. ")
    else :
        print("Ez egy sima háromszög. ")
harmadik()

def negyedik() :
    poz = input("Adja meg pozícióját: ")
    fiz = int(input("Adja meg fizetését: "))
    
    if (poz == 'vezető') :
        print(fiz * 1.25)
    else :
        print(fiz * 1.15)
negyedik()

def otodik() :
    poz = input("Adja meg pozícióját: ")
    fiz = int(input("Adja meg fizetését: "))

    while (poz != ' ') :
        if (poz == 'vezető') :
            print(fiz * 1.25)
        else :
            print(fiz * 1.15)
        break
    if (poz == ' ') :
        print("Üres pozíció")

otodik()

def hatos() :
    szam = int(input("Adjon meg egy természetes számot: "))
    for i in range(szam , -1 , -1) :
        print(i)

hatos()

def hetedik() :
    szam = int(input("Adjon meg egy természetes számot: "))
    if (szam < 0) :
        print("A feladat nem megoldható. ")
    else :
        for i in range(szam , -1 , -1) :
            print(i)
hetedik()

def nyolcas() :
    szam = int(input("Adjon meg egy természetes számot: "))
    while szam < 0 :
        szam = int(input("A feladat nem megoldható. Adjon meg egy másik számot: "))
    for i in range(szam , -1 , -1) :
        print(i)

nyolcas()

def kilences() :
    elso = int(input("Adjon meg egy számot: "))
    masod = int(input("Adjon meg egy másik számot: "))

    if (elso < masod) :
        for i in range(elso , masod + 1) :
            print(i ** 3)
    elif (elso > masod) :
        for i in range(elso , masod - 1 , -1) :
            print(i ** 3)

kilences()

def tizes() :

    szam = int(input("Adjon meg egy számot: "))
    eredmeny = 1
    for i in range(1 , szam + 1) :
        eredmeny *= i
    print(eredmeny)

    szam = int(input("Adjon meg egy számot: "))
    while szam != 0 :
        eredmeny = 1
        for i in range(1 , szam + 1) :
            eredmeny *= i
        print(eredmeny)
        break

    szam = int(input("Adjon meg egy számot: "))
    while True :
        eredmeny = 1
        for i in range(1 , szam + 1) :
            eredmeny *= i
        print(eredmeny)
        break

tizes()

def tizegy() :
    
    darab = int(input("Adjon meg egy számot: "))
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(1 , darab + 1) :
        ran = random.randint(1 , 3)
        if ran == 1 :
            count1 += 1
        elif ran == 2 :
            count2 += 1
        elif ran == 3 :
            count3 += 1
    print(f"A(z) {darab} számú randomból {count1} db 1-es, {count2} db 2-es, {count3} db 3-as lett. ")

tizegy()

def tizketto() :
    jegy = int(input("Osztályzat: "))
    count = 1
    ossz = jegy
    while jegy != 0 :
        jegy = int(input("Következő jegy: "))
        ossz += jegy
        count += 1
    atlag = ossz / (count - 1)
    print(f"{count -1} db jegyed van, átlagod {atlag}.")
    
tizketto()

def tizharom() :
    
    darab = int(input("Hány db kérdést szeretnél? "))
    countg = 0
    countw = 0

    for i in range(1 , darab + 1) :
        eredmeny = i * 10
        tipp = int(input(f"{i} * 10:"))
        if tipp == eredmeny :
            countg += 1
        else :
            countw += 1
        if countg == darab :
            print("Ügyes vagy!")
        elif countw == 3 :
            countw == 0
            atlag = (darab / 100) * countg
            print(f"Túl sok hiba! Eredmény: {darab} db kérdés, ebből helyes válasz {countg} db, rossz válasz {countw}, {atlag}% az eredmény." )
            
tizharom()