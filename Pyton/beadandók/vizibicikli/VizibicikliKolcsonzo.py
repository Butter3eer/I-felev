import datetime

class Kolcsonzes :
    def __init__(self, nev, jazon, eora, eperc, vora, vperc) :
        self.nev = nev
        self.jazon = jazon
        self.eora = int(eora)
        self.eperc = int(eperc)
        self.vora = int(vora)
        self.vperc = int(vperc)

    def __str__(self) ->str :
        return f"{self.nev} {self.jazon} {self.eora} {self.eperc} {self.vora} {self.vperc}"

    def kolcsdij(self):
        kolcsido = idoat(self.vora, self.vperc) - idoat(self.eora, self.eperc)
        if kolcsido % 1800 == 0 :
            return kolcsido // 1800 * 2400
        else:
            return int((round(kolcsido // 1800, 0) +1)) * 2400

lista = []
nevek = []

def idoat(óra, perc) :
    return óra * 3600 + perc * 60

def beolvas() :
    file = open("kolcsonzesek.txt", "r", encoding="utf-8")
    file.readline()
    for sor in file :
        reszek = sor.strip().split(";")
        nev = reszek[0]
        nevek.append(nev)
        jazon = reszek[1]
        eora = reszek[2]
        eperc = reszek[3]
        vora = reszek[4]
        vperc = reszek[5]
        
        obj = Kolcsonzes(nev, jazon, eora, eperc, vora, vperc)
        lista.append(obj)

def f5 () :
    print(f"5. feladat: Napi kölcsönzések száma: {len(lista)}")

def f6() :
    nev2 = input("6. feladat: Kérek egy nevet: ")
    print(f"\t{nev2} kölcsönzései: ")
    if nev2 in nevek :
        for item in lista :
            if item.nev == nev2 :
                elvi = f"{item.eora}:{item.eperc}"
                vivi = f"{item.vora}:{item.vperc}"
                elvitel = datetime.datetime.strptime(elvi, "%H:%M").strftime("%H:%M")
                vivitel = datetime.datetime.strptime(vivi, "%H:%M").strftime("%H:%M")
                print(f"\t{elvitel}-{vivitel}")
    elif nev2 not in nevek :
        print("\tNem volt ilyen nevű kölcsönző! ")

def f7() :
    ido = input("7. feladat: Adjon meg egy időpontot óra:perc alakban: ")
    print("\tA vizen lévő járművek: ")
    ora = ido.strip().split(":")[0]
    perc = ido.strip().split(":")[1]
    for item in lista :
        if idoat(item.eora, item.eperc) <= idoat(int(ora), int(perc)) <= idoat(item.vora, item.vperc) :
            elvi = f"{item.eora}:{item.eperc}"
            vivi = f"{item.vora}:{item.vperc}"
            elvitel = datetime.datetime.strptime(elvi, "%H:%M").strftime("%H:%M")
            vivitel = datetime.datetime.strptime(vivi, "%H:%M").strftime("%H:%M")
            print(f"\t{elvitel}-{vivitel} : {item.nev}")

def f8() :
    ossz = 0
    for item in lista :
        ossz += item.kolcsdij()
    print(f"8. feladat: A napi bevétel: {ossz} Ft")

def f9() :
    text = open("F.txt", "w", encoding="utf-8")
    for item in lista :
        if item.jazon == 'F' :
            elk = item
            elvi = f"{elk.eora}:{elk.eperc}"
            vivi = f"{elk.vora}:{elk.vperc}"
            elvitel = datetime.datetime.strptime(elvi, "%H:%M").strftime("%H:%M")
            vivitel = datetime.datetime.strptime(vivi, "%H:%M").strftime("%H:%M")
            text.write(f"{elvitel}-{vivitel} : {elk.nev}\n")

def f10() :
    print("10. feladat: Statisztika ")
    statdict = {}
    for item in lista :
        statdict[item.jazon] = statdict.get(item.jazon, 0) + 1
    sorrend = sorted(statdict.items())
    for item, ertek in sorrend :
        print(f"\t{item} - {ertek}")
    

def main() :
    beolvas()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()

main ()