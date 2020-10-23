# Definir una función que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
def numMax(num1,num2):
    if num1 > num2:
        print(num1, "es mayor que ", num2)
    else:
        print(num2, "es mayor que ", num1)

num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
numMax(num1,num2)

