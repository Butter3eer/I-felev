#elágazások
#egysezrű egyirányú elágazás : ha (feltétel)--> utasitás
"""
if feltétel:  -- ha az adott feltétel teljesül az if alatt lévő utasitás fog lefutni
    utasitás
else:           -- ha a feltétel nem teljesül(minden más esetben), akkor az else alatt lévő utasitás fut le. 
    utasitás

Mindaz, ami az if-hez tartozik(Ami a feltétel teljesülése után végre akarunk hajtani, az egy tabulátorral bentebb kezdődik)
"""

egesz= int(input("Kérek egy egész számot: "))
if egesz < 0: 
    print("A megadott szám negativ!")
    print("A szám abszolutértéke: ", (-1*egesz))
elif egesz == 0:                        # ha több feltételem van elif után berakhatok ujabb feltételeket. 
    print("A szám nulla!")
else:                                   #else mögé már nem teszünk feltételt
    print("A szám pozitív")
    print("A szám abszolutértéke: ", egesz)

#4. feladatsor: 3-7 feladatok

#logikai operátorok:
"""
LOgikai ÉS  and: akkor igaz, ha mindkét feltétel igaz
Logikai vagy  or: akkor igaz, ha legalább az egyik tag igaz
logikai tagadás negáció: not  vagy !=  

"""
A = True
B = True
if A == True and B == True:  # mivel az if-be akkor lép bele, ha true, ezért a logikai operátoroknak nemkell vkiirni, hogy mivel egyenlő, már tárolja a true-t vagy false-ot. True-ra léép be
    print("Mindkettő igaz")
if A or B:
    print("Legalább az egyik igaz")    

szam= int(input("Kérek egy számot: "))
#if not (szam>=10 and szam<=15):
if szam<10 or szam>15:
    print("Nincs benne  a [10,15] intervallumban")
else: 
    print("Nincs benne")

jelszo= input("Kérem a jelszót: ")
# jelszó: Alma226
if jelszo != "Alma26":
    print("Helytelen jelszó!")

#armstrong:
szam= int(input("szam: "))
elsoSzamJegy= szam//100
maradek= szam%100
masodikSzamJegy= maradek//10
harmadikSzamJegy= maradek%10
ossz= elsoSzamJegy**3 + masodikSzamJegy**3 +harmadikSzamJegy**3

if ossz == szam:
    print("Ez egy armstrong szám!")
else:
    print("Nem armstrong!")    



