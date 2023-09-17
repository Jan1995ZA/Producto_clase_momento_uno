#Suponiendo que cada persona promedio habla dos palabras por segundo.
# a. Pedir al usuario que diga cualquier texto real y calcular cuanto tardaria en decir esa frase.
# y cuantas palabras fueron las que dijo.
# b. si tarda mas de un minuto "decirle: para flaco tampoco te pedi un testamento"
# c. Cuanto tardaria Dalton en decirlo "Dalton habla un 30% mas rapido"

tiempo_promedo_por_dos_palabras = 2;

texto_usuario = input("Diga cualquier texto: ");
#palabras=texto_usuario.replace(" ",",");
palabras_lista = texto_usuario.split(" ");
print(palabras_lista)
numero_de_palabras = float(len(palabras_lista));
print(numero_de_palabras)
tiempo_por_palabras = numero_de_palabras/tiempo_promedo_por_dos_palabras;
print(f"\nEl tiempo que tardas en decir el texto es de {tiempo_por_palabras} seg cada dos palabras\n");
print("Punto 'a' Listo \n")
print("##########################################################")

if tiempo_por_palabras >= 60:
    print ("Para flaco, tampoco te pedi un testamento.\n");
print("Punto 'b' Listo \n")
print("##########################################################")

cuanto_tardaria_dalton = (tiempo_por_palabras*0.3)
print(f"Tardaria Dalton en decirlo {cuanto_tardaria_dalton} segundos mas rapido.\n")
print("Punto 'c' Listo \n")
print("##########################################################")
