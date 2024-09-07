import os

def menu_principal():
    os.system("cls")
    print(f""""
          MENU PRINCIPAL
          
          1.SUMAR
          2.RESTAR
          3.MULTIPLICAR
          4.DIVIDIR
          5.CONVERTIR A BINARIO
          6.CONVERTIR A OCTAL
          7.CONVERTIR A HEXADECIMAL
          8.SALIR
          """)
    
def suma():
   os.system("cls")
   primerValor = int(input("Ingrese una valor: "))
   segundoValor = int(input("Ingrese una valor: "))
   total = primerValor + segundoValor
   print(f"El valor de la suma es {total}" )
   
suma()
menu_principal()


valor1 = int(input("Ingrese el segundo valor"))
valor2 = int(input("Ingrese el primer valor"))

def sumarII(valor1, valor2):
    os.system("cls")
    total = valor1 + valor2
    print(f"el total de la suma es  {total}")
    
sumarII(valor1, valor2)
menu_principal()


def sumaIII():
    os.system("cls")
    primerValor = int(input("Ingrese el segundo valor"))
    segundoValor = int(input("Ingrese el primer valor"))
    total = primerValor + segundoValor
    return primerValor, segundoValor, total
    
primerValor, segundoValor, total = sumaIII()
print(f"la suma de {primerValor} + {segundoValor} es igual a {total}")

sumaIII()

def validarNumeroEntero(cadena):
    while True:
        try:
            numero = int(cadena)
            return numero 
        except: 
            print("Debe ingresar solo caracteres numericos")
            cadena = input("Ingrese un valor entero")