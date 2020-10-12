# https://bit.ly/36LtifW
edad = int(input("dame tu eded: "))
altura = float(input("Dame tu altura en metros: "))
peso = float(input("Dame tu peso en kilos: "))
indice = peso/(altura**2)
if indice < 22.00:
    if edad <45:
        print("Factor de riesgo bajo")
    else:
        print("Factor de riesgo medio")
if indice >= 22.00:
    if edad < 45:
        print("Factor de riesgo medio")
    else:
        print("Factor de riesgo alto")