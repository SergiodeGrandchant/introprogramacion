# E3: Escribir un programa que permita al usuario votar por dos posibles partidos políticos, A o B. Leer el partido por el que vota el usuario por teclado y mostrar el mensaje „Usted ha votado por <partido>“. En caso de que el usuario ingrese una valor incorrecto, mostrar el mensaje „Voto inválido“
partido = int(input("pon \"1\" si ti voto es para Comunidad ciudadana o pon un \"2\" si tu voto es para MAS "))
if partido == 1:
    print("tu voto fue dado para Comunidad Ciudadana")
elif partido == 2:
    print("Tu voto fue dado para MAS")
else:
    print("voto invalido")