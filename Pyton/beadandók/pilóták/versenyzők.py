import datetime

class pilotak :
    def __init__(self, nev, szuldat, nemzet, rajtsz) :
        self.nev = nev
        self.szuldat = szuldat
        self.nemzet = nemzet
        self.rajtsz = rajtsz
    
    def __str__(self) -> str:
        return f"{self.nev} {self.szuldat.date()} {self.nemzet} {self.rajtsz}"

lista = []

def beolvas() :
    global rajtsz
    file = open("pilotak.csv", "r", encoding="utf-8")
    file.readline()
    for sor in file :
        reszek = sor.strip().split(";")
        nev = reszek[0]
        szuldat = datetime.datetime.strptime(reszek[1], "%Y.%m.%d")
        nemzet = reszek[2]
        rajtsz = reszek[3]
        obj = pilotak(nev, szuldat, nemzet, rajtsz)
        lista.append(obj)

def f3() :
    print(f"3. feladat: {len(lista)}")

def f4() :
    utso = lista[-1]
    print(f"4. feladat: {utso.nev}")

def f5() :
    print("5. feladat: ")
    elobb = []
    for item in lista :
        if item.szuldat.year <= 1900 :
            elobb.append(f"{item.nev} ({item.szuldat})")

    for item in elobb :
        print(f"\t{item}")

def f6() :
    ujrajtsz = []
    for item in lista :
        if item.rajtsz != "" :
            ujrajtsz.append(int(item.rajtsz))
    min2 = min(ujrajtsz)
    nemzet2 = ""
    for item in lista :
        if  str(min2) == item.rajtsz :
            nemzet2 = item.nemzet

    print(f"6. feladat: {nemzet2}")

def f7() :
    print("7. feladat: ", end= " ")
    dict = {}
    for item in lista :
        if item.rajtsz != "" :
            dict[item.rajtsz] = dict.get(item.rajtsz, 0) + 1
    for item, rajtsz in dict.items() :
        if int(rajtsz) >= 2 :
            print(item, end=", ")
    

def main() :
    beolvas()
    f3()
    f4()
    f5()
    f6()
    f7()

main()