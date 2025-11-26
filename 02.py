class Producto_DAAC:
    def __init__(self, codigo_DAAC, nombre_DAAC, precio_DAAC, stock_DAAC):
        self.codigo_DAAC = codigo_DAAC
        self.nombre_DAAC = nombre_DAAC
        self.precio_DAAC = precio_DAAC
        self.stock_DAAC = stock_DAAC

    def tiene_stock_DAAC(self, cantidad_DAAC):
        return self.stock_DAAC >= cantidad_DAAC

    def reducir_stock_DAAC(self, cantidad_DAAC):
        if self.tiene_stock_DAAC(cantidad_DAAC):
            self.stock_DAAC -= cantidad_DAAC
            return True
        return False

    def info_DAAC(self):
        return f"{self.codigo_DAAC} - {self.nombre_DAAC}: ${self.precio_DAAC} (Stock: {self.stock_DAAC})"


inventario_DAAC = [
    Producto_DAAC("001", "Laptop", 1200, 5),
    Producto_DAAC("002", "Mouse", 25, 20),
    Producto_DAAC("003", "Teclado", 60, 15),
    Producto_DAAC("004", "Monitor", 300, 8)
]


def buscar_producto_DAAC(codigo_DAAC):
    for producto_DAAC in inventario_DAAC:
        if producto_DAAC.codigo_DAAC == codigo_DAAC:
            return producto_DAAC
    return None


def mostrar_inventario_DAAC():
    print("\n=== INVENTARIO DAAC ===")
    for producto_DAAC in inventario_DAAC:
        print(producto_DAAC.info_DAAC())
