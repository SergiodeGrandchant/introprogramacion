vec1 = []
vec2 = []
suma1 = 0
suma2 = 0
for i in range (1, 6):
    i = str(i)
    num = int(input(f"Dame le numero Nº{i} para el primer vector: "))
    vec1.append(num)
    suma1 = suma1 + num
print("-"*50)

for j in range (1, 6):
    j = str(j)
    num2 = int(input(f"Dame le numero Nº{j} para el segundo vector: "))
    vec2.append(num2)
    suma2 = suma2 + num2

res = suma1 + suma2
print("La suam de los vectores es de: ", res)