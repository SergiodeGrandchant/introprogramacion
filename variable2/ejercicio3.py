# E3: Leer el radio de un círculo por teclado y mostrar el área y perímetro del círculo en pantalla.
unidad = str(input("¿En que unidad de media tienes tu radio? "))
radio = float(input("dame el radio del circulo: "))
area = float(3.1415*radio**2)
perimetro = float(2*3.1415*radio)
respuesta = f"el radio es de: {round(radio, 2)} {unidad} el area es: {round(area, 2)} {unidad}**2 El perimetro es: {round(perimetro, 2)} { unidad}"
print(respuesta)