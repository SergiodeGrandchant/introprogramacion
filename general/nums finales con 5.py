import random
num = int(input("Dame un numero: "))
num2 = input("Dame otro numero: ")
vec = []
for i in range(1,num+1):
    num_a = random.randint(1,300)
    num_vec = str(num_a)
    numS = len(num_vec)

    if numS == 1:
        if num_vec[0] == num2:
            vec.append(num_vec)
    if numS == 2:
        if num_vec[1] == num2:
            vec.append(num_vec)
    if numS == 3:
        if num_vec[2] == num2:
            vec.append(num_vec)
print(vec)
