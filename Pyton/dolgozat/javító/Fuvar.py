import datetime

class Fuvar :
    def __init__(self, taxi, ind, tartam, táv, díj, bor, mód) :
        self.taxi = taxi
        self.ind = ind
        self.tartam = tartam
        self.táv = táv
        self.díj = díj
        self.bor = bor
        self.mód = mód
    
    def __str__(self) :
        return f"{self.taxi} {self.ind} {self.tartam} {self.táv} {self.díj} {self.bor} {self.mód}"

lista = []

def beolvas() :
    file = open("fuvar.csv", "r", encoding = "utf-8")
    file.readline()
    for sor in file :
        részek = sor.strip().split(";")
        taxi = int(részek[0])
        ind = datetime.datetime.strptime(részek[1], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        tartam = int(részek[2])
        táv = float(részek[3].replace(",", "."))
        díj = float(részek[4].replace(",", "."))
        bor = float(részek[5].replace(",", "."))
        mód = részek[6]

        obj = Fuvar(taxi, ind, tartam, táv, díj, bor, mód)
        lista.append(obj)

def f1() :
    print(f"3. feladat: {len(lista)} fuvar ")

def f2(azon) :
    db = 0
    fizu = 0
    for item in lista :
        if item.taxi == azon :
            db += 1
            fizu += item.díj + item.bor
    
    print(f"4. feladat: {db} fuvar alatt: {fizu} $")

def f3() :
    print("5. feladat:")
    fizmód = {}
    for item in lista :
        fizmód[item.mód] = fizmód.get(item.mód, 0) + 1
    
    for items, db in fizmód.items() :
        print(f"\t{items}: {db}")

def f4() :
    táv = 0
    for item in lista :
        táv += item.táv
    eredmény = táv * 1.6
    print(f"6. feladat: {round(eredmény, 2)} km")

def f5() :
    print("7. feladat: Leghosszabb fuvar: ")
    hossz = lista[0]
    for item in lista :
        if item.tartam > hossz.tartam :
            hossz = item

    print(f"\tFuvar hossza: {hossz} másodperc")
    print(f"\tTaxi azonosító: {hossz.taxi}")
    print(f"\tMegtett távolság: {hossz.táv} km")
    print(f"\tViteldíj: {hossz.díj} $")

def f6() :
    print("8. feladat: hibak.txt")
    hibas = []
    file = open("hibak.txt", "w", encoding = "utf-8")
    for item in lista :
        if item.tartam > 0 and item.díj > 0 and item.táv == 0 :
            hibas.append(item)
    hibas = sorted(hibas, key = lambda x : x.ind)
    file.write("taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n")
    for item in hibas :
        file.write(f"{item.taxi};{item.ind};{item.tartam};{item.táv};{item.díj};{item.bor};{item.mód}\n")

def main() :
    beolvas()
    f1()
    f2(6185)
    f3()
    f4()
    f5()
    f6()

main()
