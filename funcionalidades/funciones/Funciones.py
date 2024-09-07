#@autor: David Saldarriaga  
#Fecha: 04-09-2024
#Descripcion: Definicion y tipos de funciones

#Funcion sin parametros de entrada y sin parametros de salida
# nombreEstudiante = "David"
# def subTarea1(nombre):
#     print(f"Hola mundo {nombre}")
    
# subTarea1(nombreEstudiante)

# def subTarea2():
#    return "valor de uan funcion asignado a una variable"
# mensaje = subTarea2()

# print("Tarea" + mensaje)

# funcion con parametros de entrada y parametros de salida

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")

# def subtarea4(nombre, apellido):
#    mensaje = f"Hola señor {nombre} {apellido}"
#    return mensaje

# msg = subtarea4(nombre, apellido )
# print(msg)


def suma():
   primerValor = int(input("Ingrese una valor: "))
   segundoValor = int(input("Ingrese una valor: "))
   total = primerValor + segundoValor
   print(f"El valor de la suma es {total}" )
   
suma()