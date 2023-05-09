class Hiresno :
    def __init__(self, nev, nemzet, foglal) :
        self.nev = nev
        self.nemzet = nemzet
        self.foglal = foglal

    def __str__(self) :
        return f"{self.nev} {self.nemzet} {self.foglal}"

def d_feladat() :
        lista = []
        file = open("hires.txt", "r", encoding="utf-8")
        file.readline()
        for sor in file :
            reszek = sor.strip().split(";")
            nev = reszek[0]
            nemzet = reszek[1]
            foglal = reszek[2]

            obj = Hiresno(nev, nemzet, foglal)
            lista.append(obj)
        return lista

def lista_kiir() :
    lista = d_feladat()
    for item in lista :
        print(f"{item.nev:<45}" + f"| {item.nemzet:<10}" + f"| {item.foglal}")

def f_feladat(lista) :
    print("\nf) feladat: ")
    print(f"\tA híres nők száma: {len(lista)}")

def g_feladat(lista) :
    amerikai = [item for item in lista if item.nemzet == "amerikai"]
    amerikai2 = []
    for item in lista :
        if item.nemzet == "amerikai" :
            amerikai2.append(item)
    print("\ng) feladat: ")
    print(f"\tAz amerikai hírességek száma: {len(amerikai)} fő ")
    print(f"\tAz amerikai hírességek száma: {len(amerikai2)} fő ")
    print(len(list(filter(lambda x: x.nemzet=='amerikai',lista))))

def h_feladat(nemzeti) :
    
    lista = d_feladat()
    van = [item.nev for item in lista if item.nemzet == nemzeti]
    van = str(*van)

    if len(van) > 0 :
        print(f"\tVan a listában {nemzeti} nemzetiségű híresség: {van}")
    elif len(van) == 0 :
        print(f"\tNincs a listában {nemzeti} nemzetiségű híresség!")

def j_feladat(lista) :
    print("j) feladat: ")
    file = open("fizikusok.txt", "w", encoding="utf-8")
    sorrend = []
    for item in lista :
        if "fizikus" in item.foglal :
            sorrend.append(f"{item.nev} : {item.nemzet}")
    sorrend.sort()
    for item in sorrend :
        file.write(f"{item}\n")
    print("\tA fizikusok.txt állomány létrejött. ")


def main() :    
    lista_kiir()
    lista = d_feladat()
    f_feladat(lista)
    g_feladat(lista)
    print("\nh) feladat: ")
    h_feladat("horváth")
    print("\ni) feladat: ")
    h_feladat("szerb")
    j_feladat(lista)

main()