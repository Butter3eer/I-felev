import datetime

class Balkezesek:
    def __init__(self, nev, elso, utolso, suly, magassag) :
        self.nev = nev
        self.elso = elso
        self.utolso = utolso
        self.suly = suly
        self.magassag = magassag

    def __str__(self) -> str:
        return f"{self.nev} {self.elso.date()} {self.utolso.date()} {self.suly} {self.magassag}"

lista = []

def beolvas() :
    file = open("balkezesek.csv", encoding="utf-8")
    file.readline()
    for sor in file :
        reszek = sor.strip().split(";")
        nev = reszek[0]
        elso = datetime.datetime.strptime(reszek[1], "%Y-%m-%d")
        utolso = datetime.datetime.strptime(reszek[2], "%Y-%m-%d")
        suly = reszek[3]
        magassag = reszek[4]
        obj = Balkezesek(nev, elso, utolso, suly, magassag)
        lista.append(obj)


def f3() :
    print(f"3. feladat: {len(lista)}")

def f4() :
    print("4. feladat: ")
    for item in lista :
        if item.utolso.year == 1999 :
            if item.utolso.month == 10 :
                print(f"\t{item.nev}, {round(float(item.magassag) * 2.54, 1)} cm. ")

def f5() :
    global tipp
    tipp = int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
    while tipp < 1990 or tipp > 1999 :
        tipp = input("Hinbás adat! Kérek egy 1990 és 1999 közötti évszámot!: ")
        break

def f6() :
    db = 0
    db2 = 0
    for item in lista :
        if item.elso.year == tipp :
            evek = (item.utolso.year - item.elso.year) + 1
            eredmeny = evek * int(item.suly)
            db += 1
        elif item.utolso.year == tipp :
            evek2 = (item.utolso.year - item.elso.year) + 1
            eredmeny2 = evek2 * int(item.suly)
            db2 += 1
    atlag = (eredmeny + eredmeny2) / (db + db2)
    print(f"6. feladat: {round(atlag, 2)} font")
            
            
            
            


def main() :
    beolvas()
    f3()
    f4()
    f5()
    f6()

main()
