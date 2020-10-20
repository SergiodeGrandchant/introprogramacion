monto = int(input("Dame el monto que tienes: "))

bil_100 = monto // 100
print("Billenetes de 100  = ", bil_100)
monto = monto % 100

bil_50 = monto // 50
print("Billenetes de  50  = ", bil_50)
monto = monto % 50

bil_10 = monto // 10
print("Billenetes de  10  = ", bil_10)
monto = monto % 10

mon_5 = monto // 5
print("Monedas    de   5  = ", mon_5)
monto = monto % 5

mon_2 = monto // 2
print("Monedas    de   2  = ", mon_2)
monto = monto % 2

mon_1 = monto // 1
print("Monedas    de   1  = ", mon_1)
monto = monto % 1