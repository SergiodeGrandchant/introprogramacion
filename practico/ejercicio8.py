# https://bit.ly/36LtifW
num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
suma = 0
for i in range (num1+1, num2):
    print(i)
    suma = suma + i
print("la suma es: ", suma)