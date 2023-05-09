class ember :
    nev = ""
    fizu = 0

def beolvas() :
    file = open("E:\STUDY\Petrik\Pyton\órai gyakorlás, ismétlés\emberek.txt", encoding="UTF-8")
    global emberek
    emberek = []
    for sor in file :
        emb = ember()
        emb.nev = sor.split(";")[0]
        emb.fizu = int(sor.split(";")[1])
        print(emb.fizu, emb.nev)
        emberek.append(emb)

def kiir(emberek) :
    for item in emberek :
        print(item.nev , item.fizu)

def osszes(emberek) :
    osszeg = 0
    for item in emberek :
        osszeg += item.fizu
    return osszeg

beolvas()
kiir(emberek)
print(osszes(emberek))