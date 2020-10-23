#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
def caracteres(numC, caracter):
    carac = (caracter*numC)
    print(carac)

caracter = input("Dame el caracter que quires que se repita: ")
num = int(input("Dame el numeros de veces que quieres que se repita el caracter: "))
caracteres(num, caracter)