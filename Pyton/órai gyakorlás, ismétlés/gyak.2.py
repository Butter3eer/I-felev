def ot():
    lista = []
    darab = int(input("Adja meg a lista elemeinek számát: "))
    for i in range(darab) :
        lista.append(input("Lista elem: "))
    dont = input("Balra vagy jobbra tolná a listát? (b/j) ")
    if dont == "b" :
        lista.append(list[0])
        for i in range(len(lista) - 1, 0) :
            lista[i] = lista[i - 1]
        lista.remove(lista[len(lista) - 1])
    else:
        lista.insert(0, lista[len(lista) - 1])
        lista.pop(-1)
    print(lista)
ot()