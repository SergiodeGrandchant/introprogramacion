# https://bit.ly/36LtifW
num = int(input("Dame los terminos a usar"))
suma = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        signo = -1
    else:
        signo = 1
    res = signo / (1 + 2 * (i - 1))
    suma = suma + res
pi = 4 * suma
print(pi)
