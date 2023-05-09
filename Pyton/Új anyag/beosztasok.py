class tanar :
    nev = ""
    targy = ""
    oszt = ""
    oraSz= 0

def beolvas() :
    global tanarok
    global orak
    global osztalyok
    tanarok = []
    orak = []
    osztalyok = []
    file = open("beosztas.txt", encoding="UTF-8")
    while True :
        sor = file.readline().strip()
        if not sor :
            break
        else :
            ember = tanar()
            ember.nev = sor
            ember.targy = file.readline().strip()
            ember.oszt = file.readline().strip()
            ember.oraSz = int(file.readline().strip())
            tanarok.append(ember)
            orak.append(ember.oraSz)
            osztalyok.append(ember.oszt)
    file.close()

def f2() :
    print("\n2. feladat")
    print(f"A fájlban {len(tanarok)} bejegyzés van. ")
    
def f3() :
    print("\n3. feladat")
    print(f"Az iskolában a heti összóraszám: {sum(orak)}")

def f4() :
    print("\n4. feladat")
    osszesen = 0
    tanar = input("Adja meg a tanár nevét: ")
    for item in tanarok :
        if item.nev == tanar :
            osszesen += item.oraSz
    print(f"Egy tanár neve= {tanar}")
    print(f"A tanár heti óraszáma: {osszesen}")

def f5() :
    print("\n5. feladat")
    file = open("of.txt", "w", encoding="utf-8")
    sor = []
    for item in tanarok :
        if item.targy == "osztalyfonoki" :
            sor.append(item.oszt + " - " + item.nev + "\n")
    file.writelines(sor)

    file.close()

def f6() :
    print("\n6. feladat")
    osztA = input("Adja meg az osztályt: ")
    osztT = input("Adja meg a tantárgyat: ")
    tanarok2 = tanarok
    igaz = False
    for item in tanarok2 :
        if item.oszt[1] == "x" or item.oszt[2] == "x":
            if item.targy == osztT :
                if item.oszt[0] == osztA.strip(".")[0] :
                    igaz = True
    if igaz :
        print(f"Osztály= {osztA}")
        print(f"Tantárgy= {osztT}")
        print("Csoportbontásban tanulják.")
    else :
        print(f"Osztály= {osztA}")
        print(f"Tantárgy= {osztT}")
        print("Csoportban tanulják.")

def f7() :
    print("\n7. feladat")
    tanarok2 = []
    for item in tanarok :
        if item.nev not in tanarok2 :
            tanarok2.append(item.nev)
    print(f"Az iskolában {len(tanarok2)} tanár tanít. ")

def main() :
    beolvas()
    #f2()
    #f3()
    #f4()
    #f5()
    f6()
    #f7()
main()