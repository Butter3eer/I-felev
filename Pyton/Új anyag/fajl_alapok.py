def beolvas() :
    fajl = open("torpok.txt" , "r" , encoding = "UTF-8")  #open megnyitásra, meg kell adni a kiterjesztését is, illetve a nyelvet / kódolást is

    for item in fajl :
        print(item)




    """
    sor = fajl.readline() #metódus, ki tudok olvasni egy fájlból 1 sort
    print(f"elso sor:  {sor}")
    sor = fajl.readline()
    print(f"masodik sor: {sor}")
    """


def main() :
    beolvas()



main()

