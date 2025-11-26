
def menu_principal_DAAC():
    print("\n" + "=" * 40)
    print(" SISTEMA DE VENTAS DAAC")
    print("=" * 40)
    print("1. Ver inventario")
    print("2. Nueva venta")
    print("3. Ver historial de ventas")
    print("4. Salir")
    print("=" * 40)

def realizar_venta_DAAC():
    carrito_DAAC = carrito_DAAC()
    while True:
        print("\n--- NUEVA VENTA DAAC ---")
        codigo_DAAC = input("Código del producto (o 'fin' para terminar): ")
        if codigo_DAAC.lower() == 'fin':
            break

        producto_DAAC = buscar_producto_DAAC(codigo_DAAC)
        if not producto_DAAC:
            print("Producto no encontrado")
            continue

        print(producto_DAAC.info_DAAC())
        cantidad_DAAC = int(input("Cantidad: "))

        if carrito_DAAC.agregar_DAAC(producto_DAAC, cantidad_DAAC):
            print("Producto agregado al carrito")
        else:
            print("Stock insuficiente")

        carrito_DAAC.mostrar_DAAC()

    if carrito_DAAC.items_DAAC:
        confirmar_DAAC = input("\n¿Confirmar venta? (s/n): ")
        if confirmar_DAAC.lower() == 's':
            exito_DAAC, resultado_DAAC = procesar_venta_DAAC(carrito_DAAC)
            if exito_DAAC:
                print(resultado_DAAC.generar_ticket_DAAC())
            else:
                print(f"Error: {resultado_DAAC}")

def main_DAAC():
    while True:
        menu_principal_DAAC()
        opcion_DAAC = input("\nSeleccione una opción: ")

        if opcion_DAAC == '1':
            mostrar_inventario_DAAC()
        elif opcion_DAAC == '2':
            realizar_venta_DAAC()
        elif opcion_DAAC == '3':
            mostrar_historial_DAAC()
        elif opcion_DAAC == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main_DAAC()
