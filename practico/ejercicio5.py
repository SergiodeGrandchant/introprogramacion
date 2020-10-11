
pal1 = str(input("Dame una palabra: "))
pal2 = str(input("Dame otra palabra: "))
numpal1 = len(pal1)
numpal2 = len(pal2)
if numpal1 < numpal2:
    print(pal1," (", numpal1, ")", " tiene menos letras que ", "(", numpal2, ")", pal2)
elif numpal1 > numpal2:
    print(pal1," (", numpal1, ")", " tiene mas letras que ",  "(", numpal2, ")",pal2)
else:
    print("las palabras ", pal1,  "(", numpal1, ")", " y ", pal2,  "(", numpal2, ")", " tienen la misma cantidad de letras")
