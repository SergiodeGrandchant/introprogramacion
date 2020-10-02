# E5: Programar el siguiente diagrama de flujo:
num = float(input("Dame un numero: "))
print("El numero elegido fue: ", num)
if num == 0:
    print("Es cero")
elif num < 0:
    print("Es negativo")
else:
    print("Es positivo")