#Előtesztelős ciklus

import random


oldjelszo = "Majom"

jelszo = input("Kérem a jelszót: ")

while oldjelszo != jelszo :
    jelszo = input("Rossz jelszó! Adjon meg újat: ")

print("Sikeres belépés!")
# crtl + C-vel tudom megszakítani a végtelen ciklust

# Hátul tesztelős ciklus

while True :
    jelszo = input("Kérem a jelszót: ")
    if jelszo == oldjelszo :
        break

print("Sikeres belépés!")

megfelelo = False
while not megfelelo :
    jelszo = input("Kérem a jelszót: ")
    if jelszo == oldjelszo :
        megfelelo = True

#játék: 1 és 1000 közötti számot kell kitalálni

gondoltSzam = random.randit(1 , 1000)
tipp = int(input("Kérem a tippet: "))
tippekSzama = 1
while tipp != gondoltSzam :
    if tipp < gondoltSzam :
        print("Nagyobb számra gondoltam.")
    else :
        print("Kisebb számra gondoltam. ")
    tipp = int(input("Kérem a tippet: "))
    tippekSzama += 1

print(f"Sikeres találat! Tippek száma: {tippekSzama} ")

tippekszama = 0
gondoltszam = random.randint(1 , 1000)

while True :
    tippekszama += 1
    tipp = int(input("Kérem a tippet: "))
    if tipp == gondoltszam :
        break
print(f"Gratulálok, eltalálta! Tippek száma: {tippekszama} ")