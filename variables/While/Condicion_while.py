#@David	
#Fecha 28-08-2024
#Descripcion: Realizar un algoritmo para realizar la suma de valores ingresados por teclado el algoritmo 
#termina cuando el usuario cuando el usuario ingresa la letra N o n
#El algoritmo debe mostrar el total el total y el cantidad de valores ingresados
#el algoritmo debe validar la respuestacpon las letras "S", "s" O "N", "n"  de lo contrario 
#debe solicitar una nueva respuesta. El algoritmo debe validar los valores ingresados 


#Ejercicio: Pasar el ejercicio de los 5 empleados a while, validar la respuesta y validar el salario base 
contador = 0
todos_juntos = []
respuestabooleana = input(" desea ingresar un empleado? : ")

while respuestabooleana.upper() != 'NO' and respuestabooleana.upper() != 'SI':
    print("Debe ingresar  'SI' o 'NO'.")
    respuestabooleana = input("¿Desea ingresar un empleado? [SI/NO]: ")

while respuestabooleana == 'si': 
        Salario_base = float(input("Ingrese su salario base: ")) 
        identificacion = input("Ingrese su numero de identificacion: ")
        nombre_completo = input("Ingrese su nombre completo: ")
        
        while Salario_base <= 0 and not nombre_completo:
            print('Ingrese datos validos para el nombre y un salario mayor que 0 pesos')
            Salario_base = float(input("Ingrese su salario base: ")) 
            identificacion = input("Ingrese su numero de identificacion: ")
            nombre_completo = input("Ingrese su nombre completo: ")
            

        porcentaje_pension = 0.04
        porcentaje_salud = 0.045

        descuento_pension = Salario_base * porcentaje_pension
        descuento_salud = Salario_base * porcentaje_salud

        total_descuento = descuento_pension + descuento_salud
        salario_neto = Salario_base - total_descuento
        
        if salario_neto < 1200000:
            prima_extralegal = Salario_base * 0.16
        else:
            prima_extralegal = Salario_base * 0.07
        
        salario_total = salario_neto + prima_extralegal
        
        contador += 1
        
        informe = f"""El empleado {nombre_completo} con numero de identificacion  {identificacion} 
                tiene un salario base de {Salario_base:.2f}
                con deduccion por salud de {descuento_salud} y descuento por pension de {descuento_pension:.2f} 
                para un total de deducciones de {total_descuento:.2f}
                obtiene un salario neto de {salario_neto:.2f} con una prima extralegal de {prima_extralegal:.2f}
                y un sario total de {salario_total:.2f}
                -------------------------------------------------------------------------------------- 
            """
        todos_juntos.append(informe)
          
        confimacion = input("¿Desea agregar un nuevo empleado?:")
        while confimacion.upper() != 'NO' and confimacion.upper() != 'SI':
            print("Debe ingresar  'SI' o 'NO'.")
            confimacion = input("¿Desea agregar un nuevo empleado?:")
        respuestabooleana = confimacion
            
    
for item in todos_juntos:
   print(item)
print("Finalizo algoritmo!!")
        