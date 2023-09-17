
# creamos un conjunto con set.
conjunto = set(["Dato i","Dato 2"]); 
#print(type(conjunto));

# Los datos de set no son modificables.
# que pasa si queremos pasar datos modificables a no modificables.

# Metiendo un conjunto dentro de otro conjunto
## frozenset "Conjunto congelado" funcion para meter un conjunto dentro de otro
conjunto1 = frozenset(["Juan","Zapata"]); #Subconjunto de A y B
conjunto2 = frozenset([conjunto1,15,182]);  #Subconjunto de A

#En teoria de de conjuntos tenemos por un lado lo que viene siendo un conjunto 
# y por otro lado lo que viene siendo un subconjunto que es como agarrar un par
# de datos de otro conjunto 

conjunto3 = {conjunto2,"Bancolombia","CESDE"} #conjunto A

print(conjunto1); # Subconjunto de A y B y conjunto C 
print(conjunto2); # Subconjunto de A y conjunto B
print(conjunto3); # conjunto A

print(type(conjunto1)); 
print(type(conjunto2)); 
print(type(conjunto3)); 


# Teoria de conjuntos:

conjunto_a = {1,3,5,7} #Conjunto A
conjunto_b = {1,3,7} #Conjunto B
print(conjunto_a); #Conjunto A
print(conjunto_b); #Conjunto B
print(type(conjunto_a)); # tipo SET
print(type(conjunto_b)); # tipo SET

#Verificar si es un subconjunto
resultado1 = conjunto_b.issubset(conjunto_a); #issubset nos indica si es verdad que conjunto B es un subconjunto de A
resultado2 = conjunto_a.issubset(conjunto_b); #issubset nos indica si es verdad que conjunto A es un subconjunto de B
print(resultado1); 
print(resultado2); 

print(type(resultado1)); 
print(type(resultado2)); 

#Verificar si es un superconjunto

resultado3 = conjunto_a.issuperset(conjunto_b); #issuperset nos indica si es verdad que conjunto A es un superconjunto de B
resultado4 = conjunto_b.issuperset(conjunto_a); #issuperset nos indica si es verdad que conjunto B es un superconjunto de A

print(resultado3); 
print(resultado4); 

print(type(resultado3)); 
print(type(resultado4)); 


#Verificar si hay algun numero en comun
resultado5 = conjunto_b.isdisjoint(conjunto_a) #isdisjoint nos indica si hay un numero del conjunto B dentro de A

print(resultado5); # El resultado es True si en el conjunto B no hay numeros iguales dentro de A
print(type(resultado5)); 

