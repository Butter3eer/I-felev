db = int(input("Adjon meg egy db számot: "))
szavak = []

while db > 0 :
    db -= 1
    szavak.append(input("Adjon meg egy szót: "))
    if db == 0 :
        break

file = open("szavak.txt", "w", encoding = "utf-8")
for item in szavak :
    file.write(f"{item}\n")
    

def betus(darab) :
    ered = 0
    for item in szavak :
        if len(item) == darab :
            ered += 1
    if ered > 0 :
        print(f"{ered} db {darab} betűs szó van a listában. ")
    elif ered == 0 :
        print(f"Nincs a listában {darab} betűs szó. ")

betus(3)
betus(5)

mély = "aáuúoó"

for item in szavak :
    magase = True
    for betu in item :
        if betu in mély :
            magase = False
    if magase :
        print(item)