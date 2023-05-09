import random

def nevelo() :
        maganhangzo = "aáeéiíoóöőuúüű"
        if fonev[0] in maganhangzo :
            return "Az"
        else :
            return "A"

def jelzo() :
    jelzok = ["piros", "fehér", "zöld"]
    return jelzok[random.randint(0, 2)]

db = 0
for item in range(2) :
    db += 1
    fonev = input("Kérem, adjon megy egy főnevet! ")
    print(f"\t{db}. főnév: {fonev}")
    print(f"{nevelo()} {fonev} {jelzo()}.")

igaz = input("Szeretne újabb főnevet megadni? (i/n) ")

if igaz == "n" :
    print("VÉGE!")

while igaz == "i" :
    fonev = input("Kérem, adjon megy egy főnevet! ")
    db += 1
    print(f"\t{db}. főnév: {fonev}")
    print(f"{nevelo()} {fonev} {jelzo()}.")
    igaz = input("Szeretne újabb főnevet megadni? (i/n) ")
    if igaz == "n" :
        print("VÉGE!")