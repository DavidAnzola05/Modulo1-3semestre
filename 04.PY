from datetime import datetime

class Venta_DAAC:
    def __init__(self, carrito_DAAC):
        self.fecha_DAAC = datetime.now()
        self.items_DAAC = carrito_DAAC.items_DAAC.copy()
        self.total_DAAC = carrito_DAAC.total_DAAC()

    def generar_ticket_DAAC(self):
        ticket_DAAC = "\n" + "=" * 40
        ticket_DAAC += "\n TICKET DE VENTA DAAC"
        ticket_DAAC += "\n" + "=" * 40
        ticket_DAAC += f"\nFecha: {self.fecha_DAAC.strftime('%d/%m/%Y %H:%M')}"
        ticket_DAAC += "\n" + "-" * 40

        for item_DAAC in self.items_DAAC:
            ticket_DAAC += f"\n{item_DAAC.info_DAAC()}"

        ticket_DAAC += "\n" + "-" * 40
        ticket_DAAC += f"\nTOTAL: ${self.total_DAAC}"
        ticket_DAAC += "\n" + "=" * 40
        ticket_DAAC += "\n ¡Gracias por su compra!"
        ticket_DAAC += "\n" + "=" * 40

        return ticket_DAAC


historial_ventas_DAAC = []


def procesar_venta_DAAC(carrito_DAAC):
    for item_DAAC in carrito_DAAC.items_DAAC:
        if not item_DAAC.producto_DAAC.tiene_stock_DAAC(item_DAAC.cantidad_DAAC):
            return False, f"Stock insuficiente para {item_DAAC.producto_DAAC.nombre_DAAC}"

    for item_DAAC in carrito_DAAC.items_DAAC:
        item_DAAC.producto_DAAC.reducir_stock_DAAC(item_DAAC.cantidad_DAAC)

    venta_DAAC = Venta_DAAC(carrito_DAAC)
    historial_ventas_DAAC.append(venta_DAAC)

    return True, venta_DAAC


def mostrar_historial_DAAC():
    print("\n=== HISTORIAL DE VENTAS DAAC ===")

    if not historial_ventas_DAAC:
        print("No hay ventas registradas")
        return

    total_ventas_DAAC = 0
    for i_DAAC, venta_DAAC in enumerate(historial_ventas_DAAC, 1):
        print(f"\nVenta #{i_DAAC} - {venta_DAAC.fecha_DAAC.strftime('%d/%m/%Y')}: ${venta_DAAC.total_DAAC}")
        total_ventas_DAAC += venta_DAAC.total_DAAC

    print(f"\nTotal vendido: ${total_ventas_DAAC}")
