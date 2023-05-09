import datetime

def teszt() :
    mai = datetime.datetime.now()
    print(mai)
    print(f"{mai.year} {mai.month} {mai.day}")
    tegnap = datetime.datetime(2022,11,29)
    print(tegnap)
    if mai.year == tegnap.year :
        print("mindkettő esemény egy évben van")
    if mai > tegnap :
        print("nagyobb")

    datum = "2022.10.10"
    format = "%Y.%m.%d"
    d = datetime.datetime.strptime(datum, format)
    print(d)

def main() :
    teszt()

main()