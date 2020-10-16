# https://bit.ly/36LtifW
duracion = int(input("Dame las duraciones de los tramos: "))
suma_tramos = 0
while duracion > 0:
    suma_tramos = duracion + suma_tramos
    duracion = duracion + 1
    duracion = int(input("Dame las duraciones de los tramos: "))
horas = suma_tramos // 60
minutos = suma_tramos % 60
if minutos < 10:
    print("La duracion de l viaje fue de: ", horas, ":0", minutos, " horas")
elif horas == 0:
    print("La duracion de l viaje fue de: ", horas, ":0", minutos, " minutos")
else:
    print("La duracion del viaje fue de: ", horas, ":", minutos, " horas")