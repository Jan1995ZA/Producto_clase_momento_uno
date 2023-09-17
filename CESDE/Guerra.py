#lista
contador = 2; 
soldados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]; 


# Evitando que se coma una manzana con la sentencia "continue"
while  len(soldados)!=1:
    soldados.pop(contador);  
    #print(contador); 
    #contador = contador + 2; 
    #print(contador); 
    primeros = soldados[:2];  #Quitar los dos primeros elementos "técnica de rebanado"
    #print(primeros); 
    soldados = soldados[2:]  # Actualizar mi_lista sin los dos primeros elementos
    # Agregar los elementos guardados al final de mi_lista
    soldados.extend(primeros)
    print(soldados); 
    if len(soldados) ==2:
        while contador !=0:
            Ultimo = soldados[:1];  #Quitar los dos primeros elementos "técnica de rebanado"
            #print(Ultimo); 
            soldados = soldados[1:]  # Actualizar mi_lista sin los dos primeros elementos
            #print(soldados); 
            # Agregar los elementos guardados al final de mi_lista
            soldados.extend(primeros)
            contador=contador-1; 
            #print(contador); 
            #print(soldados); 
        soldados.pop(); 
        print(soldados); 
     
