class Muvesz :
    def __init__(self, nev, szulev, halev, nemzet) :
        self.nev = nev
        self.szulev = int(szulev)
        self.halev = int(halev)
        self.nemzet = nemzet

    def __str__(self) :
        return f"{self.nev} {self.szulev} {self.halev} {self.nemzet}"