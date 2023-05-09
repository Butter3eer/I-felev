print("1.1.feladat ")
byte = int(input("\tKérem, adja meg, hogy a Zoom meeting-en készült felvétel hány byte-nyi helyet foglal el a számítógépén! "))

kbyte = byte // 1024
maradek = byte % 1024
print(f"1.2.feladat\n\t{byte} B = {kbyte} KB {maradek} B ")

if byte >= 2000000 :
    print(f"1.3.feladat\n\tEzt a file-t érdemes áttennie egy külső merevlemezre. ")
elif byte < 2000000 :
    print(f"1.3.feladat\n\tEzt a file-t tegye át a Videók mappába! ")