import datetime

class Auto :
    def __init__(self, ora, perc, sec, rendsz) :
        self.ora = ora
        self.perc = perc
        self.sec = sec
        self.rendsz = rendsz

    def __str__(self) :
        return f"{self.ora} {self.perc} {self.sec} {self.rendsz}"

lista = []

def beolvas() :
    file = open("adatok.txt", "r", encoding = "utf-8")
    for sor in file :
        reszek = sor.strip().split(" ")
        ora = datetime.datetime.strptime(reszek[0], "%H").strftime("%H")
        perc = datetime.datetime.strptime(reszek[1], "%M").strftime("%M")
        sec = datetime.datetime.strptime(reszek[2], "%S").strftime("%S")
        rendsz = reszek[3]

        obj = Auto(ora, perc, sec, rendsz)
        lista.append(obj)

def fc() :
    print(f"3. feladat:\n\t{len(lista)} db adatunk van összesen. ")

def fd() :
    print("\n4. feladat:")
    if lista[-1].perc != "00" :
        max = int(lista[-1].ora) - 1

    if lista[0].perc != "00" :
        min = int(lista[0].ora) + 1

    eredmeny = max - min
    print(f"\tA mai napon dolgozott órák száma: {eredmeny} óra. ")

def fe() :
    print("\n5. feladat:")
    megora = input("\tAdjon meg egy órát: ")
    megora = datetime.datetime.strptime(megora, "%H").strftime("%H")
    file = open(f"{int(megora)}.txt", "w", encoding = "utf-8")
    for item in lista :
        if item.ora == megora :
            file.write(f"{item.ora}:{item.perc}:{item.sec} -> {item.rendsz}\n")
    if megora not in lista : 
        file.write("Ezen a napon ebben az órában nem volt áthaladás. ")
    print("\tA txt file elkészült.")
    
def main() :
    beolvas()
    fc()
    fd()
    fe()
main()