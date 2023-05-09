class Korcsolya :
    def __init__(self, nev, orszag, technikai, komponens, levonas) :
        self.nev = nev
        self.orszag = orszag
        self.technikai = float(technikai)
        self.komponens = float(komponens)
        self.levonas = int(levonas)

    def __str__(self) :
        return f"{self.nev} {self.orszag} {self.technikai} {self.komponens} {self.levonas}"

lista = []

def beolvas() :
    file = open("korcsolya.csv", "r", encoding = "utf-8")
    file.readline()
    for sor in file :
        részek = sor.strip().split(";")
        nev = részek[0]
        orszag = részek[1]
        technikai = részek[2]
        komponens = részek[3]
        levonas = részek[4]

        obj = Korcsolya(nev, orszag, technikai, komponens, levonas)
        lista.append(obj)

    for item in lista :
        print(item.nev)

def f1() :
    print(f"{len(lista)} db versenyző szerepelt. ")

def f2(orsz) :
    for item in lista :
        if item.orszag == orsz :
            return True
    return False

def f3() :
    db = 0
    for item in lista :
        if item.komponens > 1000 or item.technikai > 1000 :
            db += 1
    print(f"{db} db versenyzőnél nem számolható a pontszám. ")

def f4(név) :
    for item in lista :
        if név == item.nev :
            if item.komponens <= 1000 and item.technikai <= 1000 :
                pontok = round(item.komponens + item.technikai - item.levonas, 2)
            else :
                pontok = 0
    return pontok

def f5() :
    név = input("Adjon meg egy nevet: ")
    print(f"{f4(név)} pontja van ennek a versenyzőnek. ")

def f6() :
    file = open("tokeletesek.txt", "w", encoding="utf-8")
    for item in lista :
        if f4(item.nev) > 0 :
            file.write(f"{item.nev}: {f4(item.nev)}\n")

def main() :
    beolvas()
    f1()
    if f2("HUN") :
        print("Van ilyen nemzetiségű versenyző. ")
    else :
        print("nincs ilyen nemzetiségű versenyző. ")
    f3()
    f5()
    f6()
main()