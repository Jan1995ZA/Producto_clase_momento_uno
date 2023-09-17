#crear diccionarios con dict() (JSON_claves)

diccionario = dict(nombre = "Juan", apellido = "Zapata", edad = 15, altura = 185); 

#las listas no pueden ser claves por que son mutables y usamos 

#diccionario_lista = [frozenset(["Camilo","Zapata"]):"nombre"]; (Lista)

diccionario_frozenset = {frozenset(["Camilo","Zapata"]):"nombre"}; 

#Crear un diccionario con fromkeys: nos permite crear un diccionario con todos los valores none (sin valor o sin asignar )
diccionario_fromkeys = dict.fromkeys("ABCDE",None) #fromkeys es un metodo de diccionarios por lo tanto debe ir 
                                                            #acompañado para este caso del tipo de dato "dict"
#("ABCDE" 'itera'= variable ,None 'iguala = Dato')
#Nota:como en fromkeys itera el primer elemento se tiene que colocar como parametro una lista.

diccionario_fromkeys2 = dict.fromkeys(["nombre","apellido"]) # Esta es la forma uno

diccionario_fromkeys3 = dict.fromkeys(["nombre","apellido"],"No se") # Esta es la forma dos

print(diccionario); 
print(diccionario_frozenset); 
print(diccionario_fromkeys); 
print(diccionario_fromkeys2); 
print(diccionario_fromkeys3); 


print(type(diccionario)); 
print(type(diccionario_frozenset)); 
print(type(diccionario_fromkeys)); 
print(diccionario_fromkeys2); 
print(diccionario_fromkeys3); 




