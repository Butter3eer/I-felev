import datetime

class fogadoora :
    def __init__(self, veznev, utnev, lefogido, fogrog, fogido) :
        self.veznev = veznev
        self.utnev = utnev
        self.lefogido = lefogido
        self.fogrog = fogrog
        self.fogido = fogido
    
    def __str__(self) -> str:
        return f"{self.veznev} {self.utnev} {self.lefogido.time()} {self.fogrog.date()} {self.fogido.time()}"

lista = []

def beolvas() :
    file = open("fogado.txt", encoding="utf-8")
    for sor in file :
        reszek = sor.strip().split(" ")
        veznev = reszek[0]
        utnev = reszek[1]
        lefogido = datetime.datetime.strptime(reszek[2], "%H:%M")
        fogrogEG = reszek[3]
        fogrogRESZ = fogrogEG.split("-")
        fogrog = datetime.datetime.strptime(fogrogRESZ[0], "%Y.%m.%d")
        fogido = datetime.datetime.strptime(fogrogRESZ[1], "%H:%M")
        obj = fogadoora(veznev, utnev, lefogido, fogrog, fogido)
        lista.append(obj)

def f2() :
    print(f"2. feladat: \nFoglalások száma: {len(lista)}\n")

def f3() :
    nev = input(f"3. feladat:\nAdjon meg egy nevet: ")
    reszek2 = nev.split(" ")
    db = 0
    for item in lista: 
        if  item.veznev == reszek2[0] :
            if item.utnev == reszek2[1] :
                db += 1
    if db == 0 :
        print("A megadott néven nincs időpontfoglalás.")
    print(f"{nev} néven {db} időpontfoglalás van. ")

def f4() :
    print("\n4. feladat: ")
    ujnevek = []
    tipp = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")
    tipp2 = tipp.replace(":", "")

    fajl = open(f"{tipp2}.txt", "w", encoding="utf-8")

    tipp = datetime.datetime.strptime(tipp, "%H:%M")
    for item in lista :
        if tipp == item.lefogido :
            nev = f"{item.veznev} {item.utnev}"
            ujnevek.append(nev)

    ujnevek.sort()
    for item in ujnevek :
        print(item)
        fajl.write(f"{str(item)}\n")

def f5() :
    print("\n5. feladat: ")
    min = lista[0]
    for item in lista :
        if min.lefogido > item.lefogido :
            min = item
    minLefog = min.lefogido.strftime("%H:%M")
    minFogido = min.fogido.strftime("%H:%M")
    print(f"Tanár neve: {min.veznev} {min.utnev}")
    print(f"Foglalt időpont: {minLefog}")
    print(f"Foglalás ideje: {min.fogrog.date()}-{minFogido}")

def f6() :
    print("\n6. feladat: ")
    idopont = ["16:00","16:10", "16:20", "16:30", "16:40", "16:50", "17:00", "17:10", "17:20", "17:30", "17:40", "17:50"]
    foglalt = []
    for item in lista :
        if item.veznev == "Barna" and item.utnev == "Eszter" :
            foglaltT = item.lefogido.strftime("%H:%M")
            foglalt.append(foglaltT)
    szabad = []
    for item in idopont :
        if item not in foglalt :
            szabad.append(item)
            print(item)


 
def main() :
    beolvas()
    f2()
    f3()
    f4()
    f5()
    f6()

main()