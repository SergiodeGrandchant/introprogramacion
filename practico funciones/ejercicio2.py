# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def numMax (num1, num2, num3):
    MAX = max(num1,num2,num3)
    print("El numero mayor es: ", MAX)

num1 = int(input("dame un numero: "))
num2 = int(input("dame un numero: "))
num3 = int(input("dame un numero: "))
numMax(num1, num2, num3)
