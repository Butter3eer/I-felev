def f1() :
    egyikSzam = int(input("Adjon meg egy számot: "))
    masikSzam= int(input("Adjon meg egy másik számot: "))
    b = bool()
    b = (egyikSzam > 0) and (masikSzam > 0)
    print(f"Igaz e hogy a megadott 2 szám pozitív: {b}")

    b = (egyikSzam < 4) and (masikSzam != 6)
    print(f"Igaz e hogy az egyik szám kisebb mint 4 a másik szám pedig nem egyenlő 6-al: {b}")

    b = (egyikSzam != 0) or (masikSzam != 0)
    print(f"Igaz e hogy egyik szám egyenlő 0-val: {b}")

    b = (egyikSzam == 5) or (masikSzam != 4)
    print(f"Igaz e hogy az egyik szám egyenlő 5-el vagy a másik szám pedig nem egyenlő 4-el: {b}")

    b = (egyikSzam <= 5) or (masikSzam >= 13)
    print(f"Igaz e hogy az egyik szám nem nagyobb 5-nél vagy a másik szám nem kisebb 13-nál: {b}")

    b = (egyikSzam > 0) or (masikSzam < 0)
    print(f"Igaz e hogy az egyik szám pozitív vagy a másik szám negatív: {b}")

def f3() :
    szam = int(input("Adjon meg egy számot: "))
    eredmeny = szam % 10
    if szam % 10 == 0:
        print(f"A szám osztható 10-el. ")
    else :
        print(f"A szám nem osztható 10-el, maradéka {eredmeny} ")

def f4() :
    szam = int(input("Adjon meg egy számlálót: "))
    nev = int(input("Adjon meg egy nevezőt: "))
    if nev == 0 :
        print("Egy tört nevezője nem lehet 0. ")
    else : 
        print(f"A tört amit megadtál {szam} / {nev} ")

def f5() :
    szam = input("Adjon meg egy számot: ")
    if int(szam) == int(szam[0]) ** 3 + int(szam[1]) ** 3 + int(szam[2]) ** 3 :
        print("Ez egy Armstrong szám. ")
    else :
        print("Ez NEM egy Armstrong szám. ")

def f6() :
    szam = int(input("Adjon meg egy számot: "))
    if szam == 4 :
        print("A megadott szám a 4-es. ")
    if szam < 10 :
        print("A megadott szám kisebb mint 10. ")
    if szam % 2 == 0 :
        print("A megadott szám páros. ")
    if 0 <= szam <= 10 :
        print("A megadott szám a [0,10] intervallumba esik. ")
    if szam % 3 == 0 and szam % 5 == 0 :
        print("A megadott szám osztható 3-mal és 5-tel is. ")
    if szam < 10 and szam > 20 :
        print("A megadott szám nem a [10,20] intervallumba esik. ")

def f7 () :
    szam1 = int(input("Adjon meg egy számot: "))
    szam2 = int(input("Adjon meg egy másik számot: "))
    if szam1 == szam2 :
        print("A két szám egyenlő. ")
    if szam1 % 2 != 0 and szam2 % 2 != 0 :
        print("Mind a két szám páratlan. ")
    if szam1 % 3 == 0 or szam2 % 3 == 0 :
        print("Legalább az egyik szám osztható hárommal. ")
    if szam1 < 0 and szam2 < 0 :
        print("Mind a két szám negatív.")
    if (szam1 < 0 and szam2 >0) or (szam1 > 0 and szam2 < 0) :
        print("Az egyik szám negatív, a másik szám pozitív.")

def f8() :
    a = int(input("Adja meg az a oldal hosszát: "))
    b = int(input("Adja meg a b oldal hosszát: "))
    if a == b :
        print("Ez egy négyzet. ")
    else : 
        print("Ez egy téglalap. ")

def f9() :
    a = int(input("Adja meg a háromszög a oldalát: "))
    b = int(input("Adja meg a háromszög b oldalát: "))
    c = int(input("Adja meg a háromszög c oldalát: "))
    if a == b == c :
        print("Ez egy szabályos háromszög. ")
    else : 
        print("Ez egy hagyományos háromszög. ")

def main() :
    #f1()
    #f3()
    #f4()
    #f5()
    #f6()
    #f7()
    #f8()
    f9()
main()
