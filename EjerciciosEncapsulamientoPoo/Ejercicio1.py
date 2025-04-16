
#  Ejercicio 1 : Crear 3 objetos de Estudiante, asignar notas y mostrar los datos 
#Encapsular los atributos de un estudiante para gestionar sus notas.

class Estudiante:
    notas: list
    def __init__(self, name,notas):
        self.name = name
        self.__notas = notas
    
    def nuevas_notas(self,nuevasNotas):
        if nuevasNotas is list:
            self.__notas = nuevasNotas
        else: return 'No es una lista'
    
    def asignar_notas(self,nuevaNota):
        if 0 <= nuevaNota <= 5.0:
            self.__notas.append(nuevaNota)
            return 'Nota Asignada'
        else: return 'Nota no valida, esta fuera del rango [0,5.0]'
    
    def promedio(self):
        return f'Promedio: {round(sum(self.__notas)/len(self.__notas),2)}'
    
    def get_notas(self):
        return self.__notas


# Crear objetos de Estudiante

estudiante1 = Estudiante('Eduard', [4.5, 3.8, 4.2])
estudiante2 = Estudiante('Juan', [3.5, 4.0, 4.8])
estudiante3 = Estudiante('Maria', [4.5, 4.0, 4.2])


# Asignar nuevas notas

estudiante1.asignar_notas(4.0)

estudiante2.asignar_notas(3.0)

estudiante3.asignar_notas(5.0)


# Mostrar datos de los estudiantes

print(f'Nombre: {estudiante1.name} | Notas: {estudiante1.get_notas()} | Promedio: {estudiante1.promedio()}')

print(f'Nombre: {estudiante2.name} | Notas: {estudiante2.get_notas()} | Promedio: {estudiante2.promedio()}')
print(f'Nombre: {estudiante3.name} | Notas: {estudiante3.get_notas()} | Promedio: {estudiante3.promedio()}')

# Nuevas notas

estudiante1.nuevas_notas([4.5, 4.0, 4.2])

print(f'Notas nuevas de Eduard : {estudiante1.get_notas()}')