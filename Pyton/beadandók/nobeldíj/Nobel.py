class nobel :
    def __init__(self, ev, tipus, kernev, veznev) :
        self.ev = int(ev)
        self.tipus = tipus
        self.kernev = kernev
        self.veznev = veznev
    
    def __str__(self) -> str :
        return f"{self.ev} {self.tipus} {self.kernev} {self.veznev}"

lista = []

def beolvas() :
    file = open("nobel.csv", "r", encoding="utf-8")
    file.readline()
    for sor in file :
        reszek = sor.strip().split(";")
        ev = reszek[0]
        tipus = reszek[1]
        kernev = reszek[2]
        veznev = reszek[3]

        obj = nobel(ev, tipus, kernev, veznev)
        lista.append(obj)

def f3(ker, vez) :
    for item in lista :
        if item.kernev == ker and item.veznev == vez :
            print(f"3. feladat: {item.tipus}")
        else : 
            continue

def f4(ev, tip) :
    for item in lista :
        if item.ev == ev and item.tipus == tip :
            print(f"4. feladat: {item.kernev} {item.veznev}")
        else :
            continue

def f5() :
    print("5. feladat: ")
    for item in lista :
        if item.veznev == '' and item.ev >= 1990 :
            print(f"\t{item.ev}: {item.kernev}")
        else :
            continue

def f6(vez) :
    print("6. feladat: ")
    for item in lista :
        if vez in item.veznev :
            print(f"\t{item.ev}: {item.kernev} {item.veznev}({item.tipus})")
        else :
            continue

def f7() :
    print("7. feladat: ")
    stat = {}
    for item in lista :
        stat[item.tipus] = stat.get(item.tipus, 0) + 1
    for tipus, db in stat.items() :
        print(f"\t{tipus:<15} {db:>25} db")

def f8() :
    print("8. feladat: orvosi.txt ")
    orvos = []
    for item in lista :
        if item.tipus == "orvosi" :
            orvos.append(item)
    orvos.sort(key = lambda x : x.ev)
    file = open("orvosi.txt", "w", encoding="utf-8")
    for item in orvos :
        file.write(f"{item.ev}:{item.kernev} {item.veznev}\n")
    
def main() :
    beolvas()
    f3("Arthur B.", "McDonald")
    f4(2017, "irodalmi")
    f5()
    f6("Curie")
    f7()
    f8()
main()