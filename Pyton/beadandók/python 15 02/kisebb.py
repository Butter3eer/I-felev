elso = int(input("Kérem, adja meg a/az első negatív számot! "))
db = 1

while elso >= 0 :
    elso = int(input("Ez nem negatív szám! Kérem, adja meg mégegyszer a/az első negatív számot! "))
    db += 1
    if elso < 0 :
        print(f"\t{db}. beírt szám lett a jó. ")

masodik = int(input("Kérem, adja meg a/az második negatív számot! "))
db = 1

while masodik >= 0 :
    masodik = int(input("Ez nem negatív szám! Kérem, adja meg mégegyszer a/az első negatív számot! "))
    db += 1
    if masodik < 0 :
        print(f"\t{db}. beírt szám lett a jó. ")

if elso > masodik :
    print(f"A kisebb szám: {masodik}")
elif elso < masodik :
    print(f"A kisebb szám: {elso}")
elif elso == masodik :
    print("A két szám egyenlő. ")