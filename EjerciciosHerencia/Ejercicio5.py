#Ejercicio 5: Superclase con método __init__() y uso de super()
#Crea una clase Producto con atributos nombre y precio. Luego crea una subclase
#ProductoPerecedero que añada un atributo fecha_vencimiento.
#Requisitos:
#Usa super() para llamar al constructor de la clase base.
#Crear un objeto de ProductoPerecedero e imprimir sus atributos

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_producto(self):
        return f'Nombre: {self.nombre} | Precio: {self.precio}'

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento

    def get_producto(self):
        return f'Nombre: {self.nombre} | Precio: {self.precio} | Fecha de Vencimiento: {self.fecha_vencimiento}'

# Crear Objetos

producto1 = Producto("Leche", 2.5)
producto2 = ProductoPerecedero("Yogur", 1.5, "2023-12-01")
print(producto1.get_producto())