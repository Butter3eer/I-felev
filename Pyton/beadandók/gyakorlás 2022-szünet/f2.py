import random

lista = []

file = open("szavak.txt", "r", encoding = "utf-8")
for sor in file :
    reszek = sor.strip()
    lista.append(reszek)

vane = input("Adjon meg egy szót: ").upper()
if vane in lista :
    print(f"{vane} szó benne van a listában. ")
else :
    print("A szó nincs benne a listában. ")

def szavak() :
    elso = random.choice(lista)
    masodik = random.choice(lista)
    if elso != masodik :
        print(f"{elso} - {masodik}")
    elif elso == masodik :
        elso = random.choice(lista)
        masodik = random.choice(lista)

szavak()

folytat = input("Szeretne még váltani? (i/n) ")
while folytat == 'i' :
    szavak()
    folytat = input("Szeretne még váltani? (i/n) ")
    if folytat == 'n' :
        break