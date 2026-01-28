
def menu():
    print("1. Ingresar datos del vendedor")
    print("2. Mostrar resumen")
    print("3. Salir")           

def ingresar_datos_vendedor():  
    global cedula, nombre, vendedor, ventas, comision, valor_comision
    cedula = input("Ingrese la cédula de ciudadanía del vendedor (o -1 para terminar): ")
    if cedula == '-1':
        return False    
    nombre = input("Ingrese el nombre del vendedor: ")
    print("""
        1: Puerta a Puerta
        2: Telemercadeo
        3: Ejecutivo de ventas
        """)
    vendedor = int(input("Ingrese el tipo de vendedor (1, 2 o 3): "))
    if vendedor == 1:
        comision = 20
    elif vendedor == 2:
        comision = 15
    elif vendedor == 3:
        comision = 25
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        return True 
    ventas = float(input("Ingrese el valor de las ventas realizadas en el mes: ")) 
    valor_comision = ventas * (comision / 100)
    print("Datos del vendedor ingresados correctamente.")
    print(f"El valor a pagar por comisión es: ${valor_comision}")
    print("*"  * 70)
    return True     

def resumen():
    print("=== Resumen del Vendedor ===")
    print(f"Cédula de ciudadanía: {cedula}")
    print(f"Nombre del vendedor: {nombre}")
    print(f"Tipo de vendedor: {vendedor}")
    print(f"Valor de las ventas realizadas en el mes: ${ventas}")
    print(f"Porcentaje de comisión: {comision}%")
    print(f"Valor a pagar por comisión: ${valor_comision}")
    print("*"  * 70)    
def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            if not ingresar_datos_vendedor():
                break
        elif opcion == '2':
            resumen()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
        print("\n")      

if __name__ == "__main__":
    main()