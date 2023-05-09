class elemek :
    def __init__(self, ev, nev, vegyj, rendsz, felfed) :
        self.ev = ev
        self.nev = nev
        self.vegyj = vegyj
        self.rendsz = int(rendsz)
        self.felfed = felfed

    def __str__(self) -> str :
        return f"{self.ev} {self.nev} {self.vegyj} {self.rendsz} {self.felfed}"

lista = []
okor = []
ujkor = []

def beolvas() :
    file = open("felfedezesek.csv", "r", encoding="utf-8")
    file.readline()
    for sor in file :
        reszek = sor.strip().split(";")
        ev = reszek[0]
        nev = reszek[1]
        vegyj = reszek[2]
        rendsz = reszek[3]
        felfed = reszek[4]

        obj = elemek(ev, nev, vegyj, rendsz, felfed)
        lista.append(obj)

    for item in lista :
        if item.ev == "Ókor" :
            okor.append(item)
        else : 
            ujkor.append(item)

def f3() :
    print(f"3. feladat: Elemek száma: {len(lista)}")

def f4() :
    print(f"4. feladat: Felfedezések száma az ókorban: {len(okor)}")

def f5() :
    global tipp
    while True:
        tipp = input("5. feladat: Kérek egy vegyjelet: ")
        if (0 < len(tipp) < 3) and tipp.isalpha():
            tipp = tipp.upper()
            break

def f6() :
    print(f"6. feladat: Keresés ")
    felfed = []
    hiba = []
    for item in lista :
        if item.vegyj.upper() == tipp :
            felfed.append(item)
        elif item.vegyj.upper() != tipp :
            hiba.append(item)
    
    if len(felfed) > 0 :
        item = felfed[0]
        print(f"\tAz elem vegyjele: {item.vegyj}")
        print(f"\tAz elem neve: {item.nev}")
        print(f"\tRendszáma: {item.rendsz}")
        print(f"\tFelfedezés éve: {item.ev}")
        print(f"\tFelfedező: {item.felfed}")
    elif len(hiba) > 0 :
        print("\tNincs ilyen elem az adatforrásban! ")

def f7() :
    ev = []
    for index in range(len(ujkor)) :
        if index < len(ujkor) - 1 :
            kulonb = int(ujkor[index + 1].ev) - int(ujkor[index].ev)
            ev.append(kulonb)
    print(f"7. feladat: {max(ev)} év volt a leghosszabb időszak két elem felfedezése között. ")

def f8() :
    print("8. feladat: Statisztika ")
    stat = {}
    for item in ujkor :
        stat[item.ev] = stat.get(item.ev, 0) + 1
    for ev, db in stat.items() :
        if db > 3 :
            print(f"\t{ev}: {db} db")

def main() :
    beolvas()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()

main()