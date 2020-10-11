# https://bit.ly/36LtifW
num1 = int(input("Dame el numero: "))
divisor = 0
for divisor in range(1, num1+1):
    if num1 % divisor == 0:
        print(divisor)
