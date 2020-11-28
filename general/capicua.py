num=int(input("Dame el numero a analizar: "))
num_org = num
num_aux=num
num_arm=0


while(num>0):
    res=num%10
    num = (num-res)/10
    num_arm=num_arm*10+res


if(num_aux==num_aux):
    print(f"El numero {num_org} es un numero capicua")
else:
    print(f"El numero {num_org} no es un numero capicua")