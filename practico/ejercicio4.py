# https://bit.ly/36LtifW
num = int(input("Dame el numero de veces que quieres "))
for i in range(0, abs(num)+1):
    if num > 0:
        print(2**i)
    else:
        print(2**-i)