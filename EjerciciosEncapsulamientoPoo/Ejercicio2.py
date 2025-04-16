
# Ejercicio 2: Simular un pago y mostrar su estado - Encapsular la información de
# pago y restringir el acceso directo a los datos sensibles.

class pago:
    def __init__(self, monto):
        self.__monto = monto
        self.__estado = None
    
    def procesar_pago(self):
        if self.__monto > 0:
            self.__estado = True
            return 'Pago procesado'
        else:
            self.__estado = False
            return 'Pago no procesado'
    
    def get_estado(self):
        return self.__estado
    
# Objetos

pago1 = pago(1000)
pago2 = pago(-500) # Pago no válido

# Procesar pagos
print(pago1.procesar_pago()) 
print(pago2.procesar_pago()) 

# Ver su estado
print(f'Estado del pago 1: {pago1.get_estado()}')
print(f'Estado del pago 2: {pago2.get_estado()}')