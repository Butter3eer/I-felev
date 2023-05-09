szoveg = "Ez egy hosszú szöveg a gyakorláshoz"
szavaklistaja = szoveg.split(" ")
print(szavaklistaja)

def decTobin(dec) :
    bin = ""
    while dec > 0 :
        maradek = dec % 2
        bin = str(maradek) + bin
        dec = int(dec / 2)
    return bin
print(decTobin(4))