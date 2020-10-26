#5- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(palabra):
    tam = len(palabra)
    for indice in range(tam -1,-1,-1):
        palabraInv = palabraInv + palabra[indice]
    print(palabraInv)

palabra = input("Dame una plabra: ")
inversa(palabra)
