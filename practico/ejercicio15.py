# https://bit.ly/36LtifW
num = int(input("Dame un numero: "))
while num > 1:
    if num % 2 == 0:
        operacion = num // 2
        num = operacion
        print(operacion, " *" * operacion)
    else:
        operacion = (num * 3) + 1
        num = operacion
        print(operacion, " *" * operacion)