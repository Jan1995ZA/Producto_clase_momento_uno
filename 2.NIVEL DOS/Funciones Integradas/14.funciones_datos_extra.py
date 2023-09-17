# crear funcion de 3 parametros....
def frase(nombre,apellido,adjetivo = "guapo"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"


frase_uno = frase("Juan","Zapata","lindo"); 

print(frase_uno); 

#utilizando keyword argumento....
frase_dos = frase(adjetivo = "lindo",apellido = "Zapata",nombre ="Pablo"); 

print(frase_dos); 

#utilizando keyword argumento....
frase_tres = frase(apellido = "Zapata",nombre ="Pablo"); 

print(frase_tres); 