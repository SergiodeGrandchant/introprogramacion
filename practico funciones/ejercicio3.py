# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def letras(palabra):
    print("La palabra dada \" ", palabra, " \" consta de ", len(palabra), " letras")

palabra = input("dame la palabra que quieres que contemos: ")
letras(palabra)