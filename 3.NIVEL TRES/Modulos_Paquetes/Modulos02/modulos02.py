import Paquetes;

print(type(Paquetes)); 
print(type(Paquetes.__path__)); 

#########################################

import Paquetes.modulos_caminar,Paquetes.modulos_saludar; 

print(Paquetes.modulos_caminar.caminar("Pepito")); 
print(Paquetes.modulos_saludar.saludar("Pepito")); 

#######################################

import Paquetes.Sub_Paquete.modulos_saludar_raro;

print(Paquetes.Sub_Paquete.modulos_saludar_raro.SaludarRaro("Nimo")); 
