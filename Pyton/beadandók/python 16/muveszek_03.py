from muvesz import Muvesz 

def feladat_32() :
    lista = []
    file = open("muveszek.txt", "r", encoding = "utf-8")
    file.readline()
    for sor in file : 
        reszek = sor.strip().split(";")
        nev = reszek[0]
        evek = reszek[1].split("-")
        szulev = evek[0]
        halev = evek[1]
        nemzet = reszek[2]

        obj = Muvesz(nev, szulev, halev, nemzet)
        lista.append(obj)
    return lista

def kiir_33(lista) :
    print("3.3. feladat:\nA művészek adatai: \n")
    for item in lista :
        print(f"{item.nev:<40}" + f"| {item.szulev} " + f"| {item.halev} " + f"| {item.nemzet}")

def feladat_34(lista) :
    print(f"\n3.4. feladat:\n\tA művészek száma: {len(lista)}")

def feladat_35(lista) :
    osszes = 0
    for item in lista :
        kulomb = item.halev - item.szulev
        osszes += kulomb
    atlag = osszes / len(lista)
    print(f"\n3.5. feladat:\n\tA művészek átlagéletkora: {round(atlag, 2)}")
    
def feladat_36(lista, nemzeti) :
    x = [item.nev for item in lista if item.nemzet == nemzeti]
    x = str(*x)
    print(f"\tVan a listában {nemzeti} művész: {x}") if len(x) > 0 else print(f"\tNincs a listában {nemzeti} művész! ")

def feladat_37(lista) :
    file = open("magyarok.txt", "w", encoding = "utf-8")
    sor = []
    for item in lista :
        if item.nemzet == "magyar" :
            sor.append(item)
    sor.sort(key = lambda x : x.szulev)
    for item in sor :
        file.write(f"{item.nev} ({item.szulev} - {item.halev})\n")
    print("\n3.7. feladat:\n\tA magyarok.txt állomány létrejött. \n")

def main() :
    feladat_32()
    lista = feladat_32()
    kiir_33(lista)
    feladat_34(lista)
    feladat_35(lista)
    print("\n3.6. feladat:")
    feladat_36(lista, "osztrák")
    feladat_36(lista, "japán")
    feladat_37(lista)

main()