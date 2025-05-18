
#Ejercicio 4: Herencia Múltiple - Persona, Empleado y Deportista
#Crea tres clases:
#Persona con atributo nombre.
#Empleado con método trabajar().
#Deportista con método entrenar().
#Luego crea una clase EmpleadoDeportista que herede de ambas.

#Requisitos: Crear un objeto de EmpleadoDeportista que use ambos métodos.
#Mostrar cómo resuelve Python la herencia múltiple (orden MRO si es necesario).

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        return f'{self.nombre} está trabajando.'

class Deportista:
    def __init__(self, nombre):
        self.nombre = nombre

    def entrenar(self):
        return f'{self.nombre} está entrenando.'

class EmpleadoDeportista(Empleado, Deportista):
    def __init__(self, nombre):
        Empleado.__init__(self, nombre)
        Deportista.__init__(self, nombre)
    
    def get_nombre(self):
        return self.nombre

# Crear un objeto de EmpleadoDeportista

empleado_deportista = EmpleadoDeportista("Juan Pérez")

print(empleado_deportista.trabajar())
print(empleado_deportista.entrenar())

# Mostrar el orden de resolución de métodos (MRO)
print(EmpleadoDeportista.__mro__)