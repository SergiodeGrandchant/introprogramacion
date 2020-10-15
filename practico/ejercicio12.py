# https://bit.ly/36LtifW
nump = int(input("¿Cuantas palabras pondras? "))
larga = ""
corta = ""
for nump in range(1, nump + 1):
    pal = input("Pon la palabra aqui: ")
    if len(pal) >= len(larga):
        larga = pal
    else:
        corta = pal
print("La palabra mas larga es: ", larga)
print("La palabra mas corta es: ", corta)