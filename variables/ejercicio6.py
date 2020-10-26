#E6: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase: Tu índice de masa corporal es <valor_de_imc_va_aquí>
peso = float(input("¿Cual es tu peso? pon tu peso en kg: "))
altura = float(input("¿Cual es tu altura? ponla en metros porfavor: "))
# idmc = indice de masa corporal
idmc = peso / (altura**2)
resultado = f"Tu indice de masa corporal es de: {idmc}"
print(resultado)