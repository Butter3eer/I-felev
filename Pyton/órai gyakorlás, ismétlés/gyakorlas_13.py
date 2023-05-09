def tizharom() :
    
    darab = int(input("Hány db kérdést szeretnél? "))
    countg = 0
    countw = 0
    i = 1
    while countw < 3 and i <= darab :
        eredmeny = i * 10
        tipp = int(input(f"{i} * 10 = "))
        if tipp == eredmeny :
            countg += 1
        else :
            countw += 1
        atlag = round((countg / darab) * 100 , 2)
        i += 1
    if countw == 3 :
        print(f"Túl sok hiba! Eredmény: {darab} db kérdés, ebből helyes válasz {countg} db, rossz válasz {countw}, {atlag}% az eredmény." )
    elif countg == darab :
        print("Ügyes vagy!")
    else :
        print(f"Eredmény: {darab} db kérdés, ebből helyes válasz {countg} db, rossz válasz {countw}, {atlag}% az eredmény.")
            
tizharom()
        