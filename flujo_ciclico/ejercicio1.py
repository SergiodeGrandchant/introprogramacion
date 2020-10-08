#E1: Escribir un programa que pida al usuario ingresar un número positivo, mientras el número ingresado no sea positivo, mostrar un mensaje de error y pedir al usuario que vuela a ingresarun número.
num = float(input("Dame un numero positivo "))
while num<=0:
    print("Error valor invalido ")
    num = float(input("Dame un numero positivo"))
print("Fin")