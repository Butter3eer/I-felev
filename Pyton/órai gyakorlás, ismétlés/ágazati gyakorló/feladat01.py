ár = int(input("Adja meg a termék árát: "))
év = int(input("Adja meg ennek az éves eladási mennyiségét: "))

eredmény = round((ár * év) / 12, 2)

if eredmény >= 35000 :
    print("A termék nyereséges volt.")
elif eredmény < 35000 :
    print("A termék veszteséges volt. ")