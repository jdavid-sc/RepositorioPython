#@David	
#Fecha 28-08-2024
#Descripcion: Realizar un algoritmo para realizar la suma de valores ingresados por teclado el algoritmo 
#termina cuando el usuario cuando el usuario ingresa la letra N o n
#El algoritmo debe mostrar el total el total y el cantidad de valores ingresados
#el algoritmo debe validar la respuestacpon las letras "S", "s" O "N", "n"  de lo contrario 
#debe solicitar una nueva respuesta. El algoritmo debe validar los valores ingresados 


#Ejercicio: Pasar el ejercicio de los 5 empleados a while, validar la respuesta y validar el salario base 

suma = 0
total_valores = 0
respuesta = input("Desea seguir ingresando valore [S/N]: ")

while respuesta.upper() != 'n' :
        valor = int(input("Ingrese un valor: "))
        suma += valor
        total_valores += 1; 
        
        
