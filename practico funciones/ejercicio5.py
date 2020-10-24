#5- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

palabra = input("ingrse una frase: ")

tam = len(palabra)
tam = tam-1
palabraInv = ""
for indice in range(tam,-1,-1):
    palabraInv = palabraInv + palabra[indice]
print(palabraInv)