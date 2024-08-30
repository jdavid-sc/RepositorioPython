for i in range(1, 5+1):

    identificacion = input("Ingrese su numero de identificacion: ")
    nombre_completo = input("Ingrese su nombre completo: ")
    Salario_base = float(input("Ingrese su salario base: "))

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
    
        
    print(f"""El empleado {nombre_completo} con numero de identificacion  {identificacion} 
              tiene un salario base de {Salario_base}
              con deduccion por salud de {descuento_salud} y descuento por pension de {descuento_pension} 
              para un total de deducciones de {total_descuento}
              obtiene un salario neto de {salario_neto} con una prima extralegal de {prima_extralegal}
              y un sario total de {salario_total}
        """)
    print("-------------------------------------------------------------------------")
    
print("Finalizo algoritmo la secuencia de 5 iteraciones") 