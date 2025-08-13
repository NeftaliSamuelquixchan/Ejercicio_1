import os
def limpiar_consola():  # limpiar consola 
    if os.name == 'nt':  # limpiar consola 
        os.system('cls')  # limpiar consola 

def DATOS():  # Guardar datops
    num1 = int(input("Ingresar numero  : "))  # Guardar datos
    num2 = int(input("Ingresar numero : "))  # Guardar datos
    return num1, num2

def SUMA():  # Comando para suma 
    print("suma")
    num1, num2 = DATOS()
    resultado = num1 + num2 
    print(f"\nRESULTADO: {num1} + {num2} = {resultado}")
    input("presione Enter para continuar . . .")

def RESTA():  # Comando para resta  
     print("resta")
     num1, num2 = DATOS()
     resultado = num1 - num2 
     print(f"\nRESULTADO: {num1} - {num2} = {resultado}")
     input("presione Enter para continuar . . .")

def MULTIPLICACION():  # Comando para multiplicacion
       print("MULTIPLICACION")
       num1, num2 = DATOS()
       resultado = num1 * num2 
       print(f"\nRESULTADO: {num1} * {num2} = {resultado}")
       input("presione Enter para continuar . . .")


while True:
    limpiar_consola()
    print("1. suma")
    print("2. resta")
    print("3. ultiplicacion")
    print("4. divicion")
    opcion = input("Ingresar el numero de la opcion: ")

    if opcion == '1':
              SUMA()
    elif opcion == '2':
             RESTA()
    elif opcion == '3':
            MULTIPLICACION()
    print(f"\nSalir del sistema . . . adios")
    break
else:
        print("Opcion no valida")
        input("presione Enter para continuar . . .")
