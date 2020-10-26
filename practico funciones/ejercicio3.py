# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def contador(lista):
    contador = 0
    for i in lista:
        contador = contador + 1
    return contador


palabra = input("Dame la palabra: ")
res = contador(palabra)
print(res)

