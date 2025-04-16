class cuentaBancaria():
    def __init__(self,saldoCuenta):
        self.__saldo = saldoCuenta
    
    def set_saldo(self,nuevoSaldo):
        if nuevoSaldo >= 0:
            self.__saldo = nuevoSaldo
        else: return 'No inferior a cero'
        
    def consignar(self,monto):
        if monto >= 0:  self.__saldo += monto
        else: return 'El incremento no puede ser: x < 0'

    def retirar(self, monto):
        if 0 < monto <= self.__saldo: self.__saldo -= monto
        else: return 'El Retiro'
        
    def get_saldo(self):
        return self.__saldo
    
Acaount = cuentaBancaria(100000)
print(f'Saldo Inicial | {Acaount.get_saldo()}')

Acaount.consignar(200000)
print(f"El nuevo saldo | {Acaount.get_saldo()}")

Acaount.set_saldo(-100000)