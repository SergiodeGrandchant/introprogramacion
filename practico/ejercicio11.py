# https://bit.ly/36LtifW
from time import localtime
t = localtime()
año_ac = t.tm_year
mes_ac = t.tm_mon
dia_ac = t.tm_mday
año = int(input("En que año naciste: "))
mes = int(input("En que mes naciste: "))
dia = int(input("En que dia naciste: "))
#año
edad1 = año_ac - año
#mes
edad2 = mes_ac - mes

if edad2 < 0:
    print((edad1-1), "años")
else:
    print(edad1, "años")