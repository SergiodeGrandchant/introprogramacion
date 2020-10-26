palabra = input("ingrse una frase: ")

print(palabra)

tam = len(palabra)
tam = tam-1
print("La cantidad de letras de la palabra dada es de: ", tam)

palabraInv = ""
for indice in range(tam,-1,-1):
   print(palabra[indice], end = "")