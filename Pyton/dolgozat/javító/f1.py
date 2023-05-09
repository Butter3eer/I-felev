import math

db = int(input("Adja meg az almák számát: "))
lada = 20
eredmeny = math.ceil(db / lada)

if db % lada != 0 :
    eredmeny +=1
elif eredmeny <= 0 :
    eredmeny += 1

eleg = ""
if eredmeny < 10 :
    eleg = "nem elég"
elif eredmeny / 10 == 1 :
    eleg = "elég"
elif eredmeny % 10 != 0 :
    eleg = "több kell, mint"

print(f"Az almákhoz {eredmeny} db láda kell, ezért {eleg} 10 db láda. ")