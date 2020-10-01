# E1: Leer un número por teclado que representa una longitud en millas y mostrar el valor equivalente en kilómetros en pantalla. El mensaje debe tener el siguiente formato: “<longitud_millas> millas equivalen a <longitud_kilometros> kilómetros”
millas = float(input("dame la longitud en millas"))
km = float(millas * 1.60934)
print(millas, "millas equivalen a: ", km, "kilometros")