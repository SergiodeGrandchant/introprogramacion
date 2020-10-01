# E2: Leer dos números enteros por teclado, dividendo y divisor, y mostrar el resto de la división en pantalla. El mensaje de salida debe tener el siguiente formato: “El resto obtenido al dividir <dividendo> entre <divisor> es <resto_división>”
dividendo = int(input("dame el dividendo: "))
divisor = int(input("dame el divisor: "))
resto = dividendo % divisor
respuesta = f"El resto obtenido al dividir {dividendo} entre {divisor} es {resto}"
print(respuesta)