

# Ejercicio 4: Ingresar un producto y precio, luego mostrar el total con IVA -
# Encapsular el cálculo del total de una factura incluyendo impuestos.

class Factura:
    def __init__(self, productos):
        self.__productos = dict(productos)
        self.__precios = list(self.__productos.values())
        self.__iva = 0.19 # IVA del 19%
    
    def total(self):
        subtotal = sum(self.__precios)
        iva_total = subtotal * self.__iva
        total_con_iva = subtotal + iva_total
        return f'Total Iva incluido : {total_con_iva}'

    def get_factura(self): return f'Factura : {self.__productos}'


# objetos 

factura1 = Factura({'leche': 24499,'comida': 2032})

print(factura1.total())
print(factura1.get_factura())
