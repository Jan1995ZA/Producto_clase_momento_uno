#operadores logicos or, and y not

#AND compara uno y otro para ver si son iguales.

resultado_1 = True and False
print(f"El resultado es {resultado_1}") #False
resultado_2 = False and False
print(f"El resultado es {resultado_2}") #False
resultado_3 = False and True
print(f"El resultado es {resultado_3}") #False
resultado_4 = True and True
print(f"El resultado es {resultado_4} \n") #True

################################################

resultado_1 = True & False
print(f"El resultado es {resultado_1}") #False
resultado_2 = False & False
print(f"El resultado es {resultado_2}") #False
resultado_3 = False & True
print(f"El resultado es {resultado_3}") #False
resultado_4 = True & True
print(f"El resultado es {resultado_4} \n") #True

#OR compara uno y otro para ver cual de los dos es igual a true (True)

resultado_5= True or False
print("El resultado es", resultado_5)#True
resultado_6 = False or False
print ("El resultado es ", resultado_6 )#False
resultado_7 = False or True
print ("El resultado es " , resultado_7 )#True
resultado_8 = True or True
print ("El resultado es " , resultado_8,"\n")#True

################################################

resultado_5= True | False
print("El resultado es", resultado_5)#True
resultado_6 = False| False
print ("El resultado es ", resultado_6 )#False
resultado_7 = False | True
print ("El resultado es " , resultado_7 )#True
resultado_8 = True | True
print ("El resultado es " , resultado_8,"\n" )#True

#Not negacion del valor booleano
not_true = not True
print('el valor de la variable es igual', not_true)
not_false = not False
print ('el valor de la varible es igual ', not_false, "\n ")

