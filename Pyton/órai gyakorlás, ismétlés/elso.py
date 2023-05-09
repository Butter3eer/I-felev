print("Hello világ!")
print("A kör kerülete:", 12) #vesszővel elválasztva bármit össze tudok fűzni a kiiratásban. Alapértelmezetten szóközzel választja el 
print("A kör kerülte:", 12, sep= ",") #sep= "" elválsztja egymástól a kiirandó részeket
print("Hello", end= " ") #alapértelmezett végjel az enter, de ezt felülirhatjuk az end = "" -vel
print("világ")
#alapműveletek: 
# + - * / %(maradékos osztás) //(egész rész osztás)
print("6+5 =",6+5)
print("6-5 =",6-5)
print("6*5 =",6*5)
print("6/5 =",6/5)  #valós értékkel tér vissza
print("6//5 =",6//5) #egész részt adja vissza. NEm kerekit, levágja a maradékot
print("6%5 =",6%5) # maradékos osztás. Maradékot adja vissza
print("6**5 =",6**5) #hatványozás. Első számot emeli a második szám a kitevő

"""
több 
soros
komment
"""

#fehér karakterek: sortörés, tabulátor, időzőjel
# \n  \t  \"
print("alma\nkörte\nbarack\nszilva")
print("alma\tkörte\tbarack\tszilva")
print("\\ \"Einstein\" \\")
print("\n-------------------------------------\n")
#Adattárolás: változók létrehozása: deklarálás, első értékadás: inicializáció 
#adatok tárolása egy - egy memóriacimen történik
#Gyengén tipusos nyelv a python az adtok tárolása dinamikus. AMikor megkapja az értéket, azta tipust veszi fel

#változónév = érték
#nem kezdődhet számmal, kisbetűvel kezdődik, python konverzio összetett szavakra: elso_szam és nem lehet foglalt szó sem (pl print)
#nem használunk ékezeteket
a = 12
print(a)
print(type(a))
print(id(a))
#NE keverjük a tipusokat! Bár lehet, de ne rakjunk bele más tipust
a = 12.5  # tizedespont!!!
print(a)
print(type(a))
print(id(a))
a = 5
print(id(a))
a = a+1
print(a)

a+=1 #osszevont értékadó operátor, ugyanazt jelenti, egyel növeli az értékét
print(a)
# print("ez itt hibás") sor elején kell kezdeni az utasitást, amig nem tanulunk blokkokat!!

#szintaktikai hiba: a nyelv helyességének hibája pl prin()
#szemantikai hiba: tartalmi hiba, lefut a kód, de nem azt csinálja amit kell




