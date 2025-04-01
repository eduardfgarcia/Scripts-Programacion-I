#Ejercicio 2: Desarrollar una clase Estudiante que permita almacenar y calcular el
#promedio de las notas de un estudiante.

from abc import ABC ,abstractmethod

class Estudiante(ABC):
    notes : list
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    @abstractmethod
    def prom(self): pass

class CalcularProm(Estudiante):
    def prom(self):
        return f"Estudiante: {self.name}  |  Notas: {self.notes}  |  Promedio: {sum(self.notes) / len(self.notes)}"
    

student = CalcularProm("Eduard", [5,4,3,4])

print(student.prom())