class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Producto:
    def __init__(self,nombre,precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

def comprar_producto_cliente(cliente, producto, unidades):
    print(f"El cliente con nombre {cliente.nombre} ha comprado el producto "
        f"con nombre {producto.nombre} por un precio unitario de "
        f"{producto.precio_unitario:.2f} euros y un total de {unidades} unidades.")

cliente1 = Cliente("Juan")
producto1 = Producto("Camiseta", 15.50)
comprar_producto_cliente(cliente1, producto1, 3)