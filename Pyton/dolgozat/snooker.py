class jatekos :
    def __init__(ember, hely, nevek, orsz, nyer) :
        ember.hely = hely
        ember.nevek = nevek
        ember.orsz = orsz
        ember.nyer = nyer

    def __str__(ember) :
        return f"{ember.hely}:{ember.nevek}:{ember.orsz}:{ember.nyer}"

    
    
def beolvas() :
    file = open("snooker.txt", "r", encoding="utf-8")
    global helyezes
    global nev
    global orszag
    global nyeremeny
    lista = []
    helyezes = []
    nev = []
    orszag = []
    nyeremeny = []
    for item in file :
        lista.append(item)
        sor = item.strip()
        reszek = sor.split(";")
        helyezes.append(reszek[0])
        nev.append(reszek[1])
        orszag.append(reszek[2])
        nyeremeny.append(reszek[3])

    helyezes.pop(0)
    nev.pop(0)
    orszag.pop(0)
    nyeremeny.pop(0)

def f3() :
    print(f"3. feladat: A világranglistán {len(nev)} versenyző szerepel ")

def f4() :
    ossz = 0
    for item in nyeremeny :
        ossz += int(item)
    eredmeny = ossz / len(nyeremeny)

    print(f"4. feladat: A versenyzők átlagosan {eredmeny} fontot keresnek ")

def f5() :
    file = open("snooker.txt", "r", encoding="utf-8")
    for item in file :
        sor = item.strip()

def f6(nemzetiseg) :
    i = 0
    while i <len(versenyzok) and versenyzok[i].orszag != nemzetiseg :
        i+=1
    if i < len(versenyzok) :
        return True
    else:
        return False

def f6_2() :
    vanE=False
    for item in versenyzok :
        if item.orszag == "Norvégia" :
            print("Van norvég játékos")
            vanE = True
            break
        if not vanE:
            print("nincs norvég játékos")

def f7() :
    halmaz = set([])
    for item in versenyzok:
        halmaz.add(item.orszag)
    for item in halmaz:
        db = szamol(item)
        if db > 4:
            print(f"{item} : {db}")

def szamol(orszag) :
    db = 0
    for item in versenyzok:
        if item.orszag == orszag:
            db+=1
    return db

def f7_2() :
    stat = {}
    for item in versenyzok :
        if item.orszag not in stat:
            stat[item.orszag]=0
        stat[item.orszag]+=1
    for item in stat:
        if stat[item]>4:
            print(f"{item} : {stat[item]}")

def main() :
    beolvas()
    f3()
    f4()
    f5()
    vanE = f6("Novégia")
    f7()
main()