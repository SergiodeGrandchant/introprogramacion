
archivo = open("palabras_sencillas", "r")

listapalabraoculta=archivo.readlines()


palabra = listapalabraoculta[4]
#evita el salto de linea
palabraR = palabra.replace("\n","")
print(palabraR)
archivo.close()
