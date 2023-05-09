import statistics


def beolvas() :
    file = open("fenyoarus.csv", "r", encoding="utf-8")
    global nevek, fenyo, ar, darab, ember
    nevek = []
    fenyo = []
    ar = []
    darab = []
    ember = []
    for item in file :
        sor = item.strip()
        reszek = sor.split(";")
        nevek.append(reszek[0])
        fenyo.append(reszek[1])
        ar.append(reszek[2])
        darab.append(reszek[3])
        ember.extend(reszek)
        ar = [int(item) for item in ar]
        darab = [int(item) for item in darab]
    file.close()

def fa() :
    ujnev = []
    for item in nevek :
        if item not in ujnev :
            ujnev.append(item)
    print(f"{len(ujnev)} db ember árul fenyőt.")

def fb() :
    eredmeny = statistics.mean(ar)

    print(f"Az átlagára a fenyőknek {round(eredmeny,2)} Ft.")

def fc() :
    alar = min(ar)
    for item in range(len(ember)) :
        if ember[item] == str(alar) :
            print(f"{ember[item - 2]} árusnál a legolcsóbb a {ember[item - 1]} fenyő.")

def fd() :
    ujfenyo = []
    for item in fenyo :
        if item not in ujfenyo :
            ujfenyo.append(item)
    
    print(f"Az árusok összesen {len(ujfenyo)} db fenyőt árulnak, amik {ujfenyo}.")

def fe() :
    eredmeny = statistics.mode(fenyo)
    print(f"A leggyakoribb fenyő a(z) {eredmeny}. ")

def ff() :
    print(f"{sum(darab)} db fát árulnak összesen.")

def fg() :
    osszeg = [ar[item] * darab[item] for item in range(len(ar))]
    szemely = nevek[osszeg.index(max(osszeg))]
    print(f"{szemely} árusnak lehet a legnagyobb haszna. ")

def fh() :
    penz = int(input("Adjon meg egy összeget: "))
    if penz in ar :
        print(f"{nevek[ar.index(penz)]} boltjában talál ilyet {penz} Ft-ért. ")
    boltok = open("boltok.txt", "w", encoding="utf-8")
    boltos = nevek[ar.index(penz)]
    boltok.write(f"{boltos} ; {penz}")

def main() :
    beolvas()
    #fa()
    #fb()
    #fc()
    #fd()
    #fe()
    #ff()
    #fg()
    fh()
main()

def beolvas2() :
    file2 = open("horgaszverseny.txt", "r", encoding="utf-8")
    global azonosito, hal, tomeg, versenyzo
    azonosito = []
    hal = []
    tomeg = []
    versenyzo = []
    for item in file2 :
        sor = item.strip()
        reszek = sor.split(";")
        azonosito.append(reszek[0])
        hal.append(reszek[1])
        tomeg.append(reszek[2])
        versenyzo.extend(reszek)

def Fb() :
    print(f"{azonosito} a versenyzők azonosítója. ")

def Fc() :
    ujhal = []
    for item in hal :
        if item not in ujhal :
            ujhal.append(item)
    halak = open("halak.txt", "w", encoding="utf-8")
    halak.write(f"{ujhal}")
    print(f"{ujhal} halakat fogtak a versenyzők. ")

beolvas2()
Fb()
Fc()

#elnézést kérek, de nem volt időm befejezni a hétvégén a javítást, mert dolgoznom kellett tanulás mellett
#illetve nem emlékszem hogy lehetett e statisztikát használni itt szóval ha anélkül kellett volna szívesen megcsinálom olyan módon is