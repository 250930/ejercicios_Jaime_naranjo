def menu():
    print("=== Menú de Liquidación de Servicio de Matrícula ===")
    print("1. Ingresar datos del estudiante")
    print("2. Mostrar resumen")
    print("3. Salir")




def ingresar_datos_estudiante():
    global valor_final,nombre_estudiante, carrera, beca, valor_matricula, descuento
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    
    print("""
        1: Técnico en Sistemas
        2: Técnico en Desarrollo de videojuegos
        3: Técnico en Animación Digital
        """)
    carrera = int(input("Ingrese el número de la carrera: "))
    
    if  carrera == 1:
        valor_matricula = 800000
    elif carrera == 2:
        valor_matricula = 1000000
    elif carrera == 3:
        valor_matricula = 1200000

    
    print("""
1: Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.
2: Beca Cultural – Deportes. Descuento del 40% sobre el valor matrícula
3: Sin Beca.
        """)
    beca = int(input("ingrese el numero de beca (1, 2 o 3): "))
    if beca == 1:
        descuento = 50
    elif beca == 2:
        descuento = 40
    elif beca == 3:
        descuento = 0
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        return
    print("Datos del estudiante ingresados correctamente.")
    
    valor_final = valor_matricula - (valor_matricula * (descuento / 100))
    print("Liquidación calculada correctamente.")
    print(f"El valor final a pagar es: ${valor_final}")
    print("*"  * 70)

    
def mostrar_resumen():
    print("=== Resumen de Liquidación ===")
    print(f"Nombre del estudiante: {nombre_estudiante}")
    print(f"Valor de la matrícula: ${valor_matricula}")
    print(f"Porcentaje de descuento: {descuento}%")
    print(f"Valor final a pagar: ${valor_final}")
    print("*"  * 70)

def main():
    while True:
        menu()
        opcion = int(input("Seleccione una opción (1-3): "))
        if opcion == 1:
            ingresar_datos_estudiante()
        elif opcion == 2:
            mostrar_resumen()
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            return opcion

if __name__ == "__main__":
    main()