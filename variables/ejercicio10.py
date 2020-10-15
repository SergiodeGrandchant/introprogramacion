# E10: Leer un número de la entrada y el nombre del usuario, mostrar el mensaje “Éxito!!!” en la pantalla, si es que el número es un múltiplo de 7 y el nombre es “Juan” o “Pablo”.
num = int(input("dama un numero: "))
nombre = str(input("¿Cual es tu nombre? "))
if num % 7 == 0 and (nombre == "Pablo" or nombre == "Juan"):
    print("Éxito!!!")
else:
    print("FIN")