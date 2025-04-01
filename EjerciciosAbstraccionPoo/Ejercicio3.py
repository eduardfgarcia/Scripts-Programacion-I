#Ejercicio 3: Crear una clase Factura que permita registrar productos y calcular el
#total de a compra

from abc import ABC, abstractmethod
import random

class Factura(ABC):
    productos: list
    def __init__(self, productos):
        self.productos = productos

    @abstractmethod
    def method(): pass 

class RegstrarCalcularProductos(Factura):
    def method(self):
        facturaResult = dict()
        for i in self.productos: facturaResult[i] = random.randint(1000,10000)
        totalCompra = list(facturaResult.values())
        return f'Productos: {facturaResult}  |  Total A pagar: {sum(totalCompra)}$'
            
factura1 = RegstrarCalcularProductos(["Leche","Papas","Gaseosas","Ropas"])

print(factura1.method())
        