# Ejercicio 1    |    Desarrollar Crear una clase Empleado que permita calcular el salarios de los empleados

from abc import ABC, abstractmethod 

class Empleado(ABC):
    name: str
    salario_bruto: float
    def __init__ (construct, name, salario_bruto):
        construct.name = name
        construct.salario_bruto = salario_bruto
        construct.cotizaciones = [0.8,0.15]
        
    @abstractmethod
    def calcular(construct): pass

class SalarioQuincenal(Empleado): 
    def calcular(construct): return f'Empleado: {construct.name}  |  alario Quincenal/Bruto: {construct.salario_bruto}'

class SalarioMensual(Empleado):
    def calcular(construct):
        salarioMensual = construct.salario_bruto * 2 
        return f'Empleado: {construct.name}  |  Salario Mensua: {round(salarioMensual)}'
    
class SalarioDiario(Empleado):
    def calcular(construct):
        salarioDiario = (construct.salario_bruto *2) / 30
        return f'Empleado: {construct.name}  |  Salario Diario: {round(salarioDiario)}'

class ValorNeto(Empleado):
    def calcular(construct):
        seguroMedico = 50##
        seguridadSocial, impuestoRenta = [*construct.cotizaciones]
        calcule = sum([construct.salario_bruto * seguridadSocial, construct.salario_bruto * impuestoRenta, seguroMedico])
        return f'Empleado: {construct.name}  |  Sueldo Neto: {round(calcule)}$'
    

empleado1 = ValorNeto("Eduard Garcia",2000)

print(empleado1.calcular())
