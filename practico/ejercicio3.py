# https://bit.ly/36LtifW
dividendo = int(input("Dame el dividendo: "))
divisor = int(input("Dame el divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo % divisor == 0:
    print("La division dada es exacta")
else:
    print("La division dada no es exacta")
print("El cociente es: ", cociente)
print("El resto es: ", resto)