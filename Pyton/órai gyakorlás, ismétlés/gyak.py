"""
def maxi(a , b) :
    if a > b :
        return a
    else :
        return b

def main() :
    x = int(input("Add meg az első számot: "))
    y = int(input("Add meg a másik számot: "))
    print(maxi(x, y))
    
main()
"""

def faktoriális(n) :
    eredmeny = 1
    for i in range(1 , n + 1) :
        eredmeny *= i
    return eredmeny

def feladat() :
    x = int(input("Add meg a számot: "))
    print(faktoriális(x))

feladat()

"""
import random


def f2() :
    logikaiak = []
    for i in range(7) :
        if random.randint(1, 2) == 1 :
            logikaiak.append(True)
        else :
            logikaiak.append(False)
    print(*logikaiak)
f2()
"""
def main() :
    l = [0,1,5,50,46,89,24,57,33]
    
    def kiirtartalom(l) :
        for i in l :
            print(i)
        
    def kiirrange(l) :
        for i in range(len(l)) :
            print(l[i])

    def kiirstring(l) :
        for c in l :
            print(c)

    kiirtartalom(l)
    print("___________")
    kiirrange(l)
    print("___________")
    kiirstring("Jó reggelt kívánok")

main()
