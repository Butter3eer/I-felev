import random


file = open("elemek.txt", "r", encoding = "utf-8")

lista = []

for sor in file :
    elemek = sor.strip()
    lista.append(elemek)

print(f"{len(lista)} db elem van a fáljban. ")
print(f"{lista[-1]} az utolsó elem. ")

def kereses(elem) :
    if elem not in lista :
        return False
    return True

elem = input("Adjon meg egy elemet: ")

if kereses(elem) == True :
    print("Van ilyen elem a listában. ")
elif kereses(elem) == False :
    print("Nincs ilyen elem a listában. ")

def ajánlás() :
    return random.choice(lista)

print(ajánlás())