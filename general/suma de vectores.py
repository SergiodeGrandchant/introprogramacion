vec1 = []
vec2 = []
vecS = []
suma1 = 0
suma2 = 0
for i in range (1, 6):
    i = str(i)
    num = int(input(f"Dame le numero Nº{i} para el primer vector: "))
    vec1.append(num)
print("-"*50)

for j in range (1, 6):
    j = str(j)
    num2 = int(input(f"Dame le numero Nº{j} para el segundo vector: "))
    vec2.append(num2)

for ñ in range (0, 5):
    suma = vec1[ñ] + vec2[ñ]
    vecS.append(suma)


print(vec1)
print(vec2)
print(vecS)
