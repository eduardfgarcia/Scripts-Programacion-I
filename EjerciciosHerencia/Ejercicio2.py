#Ejercicio 2: Herencia con método sobrescrito - Animal y Perro
#Crea una clase base Animal con un método hacer_sonido(). Luego crea una
#subclase Perro que sobrescriba ese método para imprimir "Guau".
#Requisitos:
#Crear otra subclase, Gato, que también sobrescriba el método con "Miau".
#Crear un objeto de cada clase e invocar hacer_sonido().



class Animal:
    def __init__(self):
        self.nombreAnimal = 'Animal'
    
    def hacer_sonido(self): return f'Animal: {self.nombreAnimal} | Sonido: {self.sonido()}'

class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.nombreAnimal = 'Dog'
    
    def hacer_sonido(self): return f'Guau  |  Animal: {self.nombreAnimal}'

class Gato(Animal):
    def __init__(self):
        super().__init__()
        self.nombreAnimal = 'Cat'
    
    def hacer_sonido(self): return f'Miau  |  Animal: {self.nombreAnimal}'


perro1 = Perro()
gato1 = Gato()
print(perro1.hacer_sonido())
print(gato1.hacer_sonido())
    