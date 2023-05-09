def beolvas2() :
    file = open("E:\STUDY\Petrik\Pyton\órai gyakorlás, ismétlés\emberek.txt", encoding="UTF-8")
    global nevek
    global fizuk
    nevek = []
    fizuk = []
    for sor in file :
        nev = sor.split(";")[0]
        nevek.append(nev)
        fizuk.append(int(sor.split(";")[1]))

def kiir2(nevek, fizuk) :
    for item in range(len(nevek)) :
        print(f"név: {nevek[item]}, fizu: {fizuk[item]}")

def main() :
    beolvas2()
    
main()