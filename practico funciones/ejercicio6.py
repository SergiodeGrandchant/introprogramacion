#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
palabra = input("ingrese una frase: ")

tam = len(palabra)
tam = tam-1
palabraInv = ""
for indice in range(tam,-1,-1):
    palabraInv = palabraInv + palabra[indice]

if palabraInv == palabra:
    print(palabra, " = TRUE")
else:
    print(palabra, " = FALSE")