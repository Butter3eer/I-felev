lista = [2,5,18,91,23,5] #van első, második, stb elem benne, lehet benne ismétlődés
#az index helyek 0-val kezdődnek, szóval itt az 1 indexhely az 5-ös
print(lista)
print(*lista)# a * csak a lista elemeit írja ki, a [] nem fog látszódni
print(*lista, sep = "; ")
print(lista[2]) #[2] ha a 2-es index helyen levő elemet akarod kiíratni
x = int(input("Hanyadik számot szeretnéd? "))
if x > len(lista) :
    print("Nincs ennyi elem a listában. ")
else:
    print(lista[x - 1]) #mivel 0-nál kezdődik az index száma az elemeknek ezért egyet le kell vonni
lista2 = [] #így csinálsz üres listát
print(len(lista2))  #len() egy megadott lista hosszát tudod lekérni
lista3 = [1,2,"alma", True, 1.2, "körte"] #mindegy az adat típus, benne lehetnek 1 listában
sumlist = lista + lista3 #egymás után írja le az összeadott listákat
print(*sumlist)
multlist = lista * 3 #egymás mögé rakja be a listát 3x
print(*multlist)
print(2 in lista) #logikai változó, boolean, True vagy False lesz a válasz
if 2 in lista :
    print("A 2 benne van a listában. ")
print(2 not in lista)
print(lista[2 : 4]) #index számtól index számig írja ki az értékeket
print(lista[2: ]) #2-es index helytől írja ki az összes elemet
print(lista[:3]) #a felső érték (3) már nem lesz benne 
lista[2] = 100  #módosítja az adott indexű elemet a listában
print(*lista)
lista.append(500) #hozzáfűzés a lista végére
print(*lista)


nevek = []
def feltolt(nevek) :
    n = int(input("Hány név van a listában: "))
    for i in range(n) :
        nevek.append(input("Add meg a kövi nevet: "))

def kiir(l) :
    for i in l :
        print(i)

feltolt(nevek)
kiir(nevek)

neveka = []
#feltolt(neveka)
nevekb = []
feltolt(nevekb)
nevekc = []
#feltolt(nevekc)

kiir(nevekb)
nevekb.insert(2 , "Kázmér") #be lehet szúrni az index helyre egy adatot anélkül hogy kiszedné az adott index helyén levő eredeti elemet
kiir(nevekb)
#nevekb.clear()  #ezzel törlünk elemeket listából
nevek.pop(2)
kiir(nevekb)
nevekb.remove("Kázmér")
kiir(nevekb)