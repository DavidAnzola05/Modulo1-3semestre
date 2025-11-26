class ItemCarrito_DAAC:
    def __init__(self, producto_DAAC, cantidad_DAAC):
        self.producto_DAAC = producto_DAAC
        self.cantidad_DAAC = cantidad_DAAC

    def subtotal_DAAC(self):
        return self.producto_DAAC.precio_DAAC * self.cantidad_DAAC

    def info_DAAC(self):
        return f"{self.producto_DAAC.nombre_DAAC} x{self.cantidad_DAAC} = ${self.subtotal_DAAC()}"


class Carrito_DAAC:
    def __init__(self):
        self.items_DAAC = []

    def agregar_DAAC(self, producto_DAAC, cantidad_DAAC):
        if producto_DAAC.tiene_stock_DAAC(cantidad_DAAC):
            item_DAAC = ItemCarrito_DAAC(producto_DAAC, cantidad_DAAC)
            self.items_DAAC.append(item_DAAC)
            return True
        return False

    def total_DAAC(self):
        total_DAAC = 0
        for item_DAAC in self.items_DAAC:
            total_DAAC += item_DAAC.subtotal_DAAC()
        return total_DAAC

    def mostrar_DAAC(self):
        print("\n=== CARRITO DAAC ===")
        if not self.items_DAAC:
            print("Carrito vacío")
            return
        for item_DAAC in self.items_DAAC:
            print(item_DAAC.info_DAAC())
        print(f"\nTOTAL: ${self.total_DAAC()}")

    def vaciar_DAAC(self):
        self.items_DAAC = []
