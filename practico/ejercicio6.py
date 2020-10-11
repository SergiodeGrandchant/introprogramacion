# https://bit.ly/36LtifW
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
min = min(num1, num2)
max = max(num1, num2)
if min != max:
    print(min, "  ", max)
else:
    print("Los numeros son iguales")

