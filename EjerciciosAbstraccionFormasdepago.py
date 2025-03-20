from abc import ABC, abstractmethod 

class formasDePago(ABC):
    user : str
    password : int
    def __init__(self,user,password):
        self.user = user
        self.password = password

    @abstractmethod
    def pagar(self): pass

class efectivo(formasDePago):
    def pagar(self): return f"El Usuario {self.user}. con cotraseña {self.password} va a pagar el producto en Efectivo"


class tarjetaDebito(formasDePago):
    def pagar(self): return f"El Usuario {self.user}. con cotraseña {self.password} va a pagar el producto con Tarjeta Debito"

class tarjetaCredito(formasDePago):
    def pagar(self): return f"El Usuario {self.user}. con cotraseña {self.password} va a pagar el producto con tarjetaCredito"

class nequi(formasDePago):
    def pagar(self): return f"El Usuario {self.user}. con cotraseña {self.password} va a pagar el producto forma Nequi"

class PayPal(formasDePago):
    def pagar(self): return f"El Usuario {self.user}. con cotraseña {self.password} va a pagar el producto forma PayPal"



person1 = efectivo("Eduard Garcia",1070596978)

print(person1.pagar())