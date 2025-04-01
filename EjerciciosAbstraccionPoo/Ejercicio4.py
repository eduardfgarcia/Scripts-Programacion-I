#Ejercicio 4: Diseñar una clase Usuario para gestionar autenticaciones en un sistema.

from abc import ABC, abstractmethod
import random

class Usuario(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod
    def autenticator(self): pass

class CifradoContraseñaBin(Usuario):
    def autenticator(self): return bin(self.password)[2:]

class CambiarContraseña(Usuario):
    def autenticator(self):
        print("\t-  Cambia Tu Contraseña...\n\n")
        if self.password:
            newPassword = int(input("\t-  Ingrese su nueva contraseña :: "))
            self.password = newPassword
        return f"Su Contraseña ha sido cambiada a: {self.password}"



user = CifradoContraseñaBin("Eduard",2905)
print(user.autenticator())