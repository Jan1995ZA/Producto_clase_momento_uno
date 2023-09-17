#Encontrando el numero mayor
nuemros = [4,7,8,9]; 

print(max(nuemros)); 
print(min(nuemros)); 
print("\n"); 
#Redondeando  a 6 a decimales
numero = round(10.2555158 * 100); 
print(numero/100); 

#Redondeando  a 6 a decimales
numero = round(10.2555158,0); 
print(numero); 

#Redondeando  a 6 a decimales
numero = round(10.2555158,3); 
print(numero); 
print("\n"); 
# Funcion bool: retorna "False" en caso que le pasemos un 0,un dato vacio, False o ninguno
resultado = bool(0); 
print(resultado); 
resultado = bool(""); 
print(resultado); 
resultado = bool(); 
print(resultado); 
resultado = bool(False); 
print(resultado); 
resultado = bool(None); 
print(resultado); 
print("\n"); 

#bool con datos no vacios es True
resultado = bool(1); 
print(resultado); 
resultado = bool(" "); 
print(resultado); 
resultado = bool("Blanco"); 
print(resultado); 
resultado = bool(True); 
print(resultado);  
print("\n"); 

# Funcion all : retorna True, si todos lo valores son verdaderos
# en vez de comprobar un solo elemento comprueba lo que esta adentro de una iterable.

resultado_all = all([234,True,[2,3,5]]); 
print(resultado_all); 
resultado_all = all([0,False,[None,3,5]]); 
print(resultado_all); 

#Funcion sum: sema todos los valores de un iterable
suma_total = sum(nuemros)
print(suma_total); 