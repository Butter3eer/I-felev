#Még az új anyaghoz (lista.py)
lista = [1,2,3,4,5]
print(lista[-1]) #utolsó elemet így lehet kiíratni ha nem tudod mennyi elemet tartalmaz az eredeti lista
print(lista[len(lista)-1])

#GYAKORLÁS
import random
#1. FEl
#lotto
def lottoSorsol() :
    szamok = []
    for i in range(5) :
        while True :
            x= random.randint(1 , 95) #vigyázz, mind a 2 vége beletartozik a range-be a for ciklussal szemben
            if x not in szamok : #megszabja hogy ne lehessen 2 egyforma számot sorsolni
                break
        szamok.append(x)
    return szamok

def main() :
    for i in range(52) :
        s1 = lottoSorsol()
        s1.sort() #sort az szortírozza az értékeket a listában, alapból növekvő sorrendbe rakja a számokat
        print((i + 1), ". hét: ", end = "")
        print(*s1)
main()