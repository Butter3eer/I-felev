import datetime

class kutyafajtak :
    def __init__(self, id, nev, ognev) :
        self.id = int(id)
        self.nev = nev
        self.ognev = ognev

    def __str__(self) :
        return f"{self.id} {self.nev} {self.ognev}"

class kutyak :
    def __init__(self, id, fajtaid, nevid, kor, utorvos) :
        self.id = int(id)
        self.fajtaid = int(fajtaid)
        self.nevid = int(nevid)
        self.kor = int(kor)
        self.utorvos = utorvos

    def __str__(self) :
        return f"{self.id} {self.fajtaid} {self.nevid} {self.kor} {self.utorvos.time()}"

class kutyanevek :
    def __init__(self, id, nev) :
        self.id = id
        self.nev = nev

    def __str__(self) :
        return f"{self.id} {self.nev}"

kutyafaj = []
kutyaK = []
kutyanev = []

def beolvas() :
    file1 = open("KutyaFajtak.csv", "r", encoding = "utf-8")
    file2 = open("Kutyak.csv", "r", encoding = "utf-8")
    file3 = open("KutyaNevek.csv", "r", encoding = "utf-8")
    file1.readline()
    file2.readline()
    file3.readline()
    for sor1 in file1 :
        reszek1 = sor1.strip().split(";")
        id = reszek1[0]
        nev = reszek1[1]
        ognev = reszek1[2]

        obj = kutyafajtak(id, nev, ognev)
        kutyafaj.append(obj)

    for sor2 in file2 :
        reszek2 = sor2.strip().split(";")
        id = reszek2[0]
        fajtaid = reszek2[1]
        nevid = reszek2[2]
        kor = reszek2[3]
        utorvos = datetime.datetime.strptime(reszek2[4], "%Y.%m.%d").strftime("%Y.%m.%d")

        obj = kutyak(id, fajtaid, nevid, kor, utorvos)
        kutyaK.append(obj)

    for sor3 in file3 :
        reszek3 = sor3.strip().split(";")
        id = reszek3[0]
        nev = reszek3[1]

        obj = kutyanevek(id, nev)
        kutyanev.append(obj)
    
def f3() :
    print(f"3. feladat: Kutyanevek száma: {len(kutyanev)}")

def f6() :
    kor = []
    for item in kutyaK :
        kor.append(item.kor)
    eredmeny = round(sum(kor) / len(kutyaK), 2)
    print(f"6. feladat: Kutyák átlag életkora: {eredmeny}")

def f7() :
    idos = kutyaK[0]
    idosnev = ""
    idosfaj = ""
    for item in kutyaK :
        if idos.kor < item.kor :
            idos = item
    for item in kutyanev :
        if int(item.id) == int(idos.nevid) :
            idosnev = item.nev
    for item in kutyafaj :
        if idos.fajtaid == item.id :
            idosfaj = item.nev
    print(f"7. feladat: Legidősebb kutya neve és fajtája: {idosnev}, {idosfaj}")

def f8() :
    print("8.feladat: Január 10.-én vizsgált kutya fajták: ")
    stat = {}
    for item in kutyaK :
        if item.utorvos == "2018.01.10" :
            stat[item.fajtaid] = stat.get(item.fajtaid, 0) + 1
    for fajtaid, db in stat.items() :
        for item in kutyafaj :
            if fajtaid == item.id :
                fajtaid = item.nev
                print(f"\t{fajtaid}: {db} kutya ")

def f9() :
    stat = {}
    nagy = 0
    for item in kutyaK :
        stat[item.utorvos] = stat.get(item.utorvos, 0) + 1
    for item, db in stat.items() :
        if nagy < db :
            nagy = db
    print(f"9. feladat: Legjobban leterhelt nap: {max(stat, key = stat.get)}: {nagy} kutya")

def f10() :
    file = open("Névstatisztika.txt", "w", encoding="utf-8")
    vizsgalt = []
    for item in kutyaK :
        for adat in kutyanev :
            if int(item.nevid) == int(adat.id) :
                vizsgalt.append(adat.nev)
    vizsdict = {}
    for item in vizsgalt :
        vizsdict[item] = vizsdict.get(item, 0) + 1
    szort = sorted(vizsdict.items(), key = lambda x : -x[1])
    for items, db in szort :
        file.write(f"{items}; {db}\n")

def main() :
    beolvas()
    f3()
    f6()
    f7()
    f8()
    f9()
    f10()

main()