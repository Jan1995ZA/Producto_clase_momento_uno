diccionario = {
    "nombre": "Juan",
    "apellido":"zapata",
    "ingresos_mensuales": 80_000_000
}

for key in diccionario:
    print(key); # cuando ponemos key muestra la clave
    
else:
    print("\n"); 
    print("Termino el bucle."); 

print("\n"); 

#para mostrar el valor de la clave utilizamos el metodo "items()" permitiendo recorrer el elemento y nos deveulve una tupla
# que hace referencia a la clave y el valor.
for datos in diccionario.items():
    
    key_ = datos[0]; 
    valor_ = datos[1]; 
    
    print(f"{key_}: {valor_}"); 
    
    
else:
    print("\n"); 
    print("Termino el bucle."); 
    
print("\n"); 