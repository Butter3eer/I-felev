valt = int(input("Adja meg a Ft - Eur váltószámát: "))
egys = input("Adja meg mibe kívánja ezt váltani (Ft/Eur):")
        
if egys == "Ft" or egys == "Eur" :
    ossz = int(input("Adja meg a váltani kívánt összeget: "))

    if egys == "Eur" :
        eredmeny = round(ossz / valt, 2)
        print(f"A váltás eredménye: {eredmeny} EUR")
    elif egys == "Ft" :
        eredmeny = int(ossz * valt)
        print(f"A váltás eredménye: {eredmeny} Ft")
else :
    print("Nincs ilyen pénznem a programban vagy nem is létezik.")