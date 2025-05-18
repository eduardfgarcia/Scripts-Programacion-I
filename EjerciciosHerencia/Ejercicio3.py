#Ejercicio 3: Herencia Jerárquica - Vehículos
#Crea una clase Vehiculo con atributos marca y modelo. Luego crea dos subclases:
#Carro, que añade número_de_puertas.
#Moto, que añade tipo_de_motor.
#Requisitos:
#Crear objetos de ambas subclases e imprimir todos sus atributos.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def get_vehiculo(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo}'

class Carro(Vehiculo):
    def __init__(self,marca,modelo,numPuertas):
        super().__init__(marca,modelo)
        self.numPuertas = numPuertas
    
    def get_vehiculo(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Numero de Puertas: {self.numPuertas}'

class moto(Vehiculo):
    def __init__(self,marca,modelo,motor):
        super().__init__(marca,modelo)
        self.motor = motor
    
    def get_vehiculo(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Numero de Puertas: {self.numPuertas} | Motor: {self.motor}'


    
