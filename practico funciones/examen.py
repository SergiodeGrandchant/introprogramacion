
def caracteres(numC, caracter):
   for i in range(1,numC+1):
       print(caracter,end="")

caracter = input("Dame el caracter que quires que se repita: ")
num = int(input("Dame el numeros de veces que quieres que se repita el caracter: "))
caracteres(num, caracter)