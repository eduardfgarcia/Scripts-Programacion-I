

# Ejercicio 5: Probar cada opción cambiando el valor con el setter y ejecutando la
# acción - Encapsular una selección de opciones, permitiendo acceder y modificar la
# opción elegida de forma controlada.

class SelectorOpciones:
    def __init__(self, opciones, opcion_inicial=None):
        self.__opciones = list(opciones)  # Encapsulamos la lista de opciones
        self.__opcion_seleccionada = None
        if opcion_inicial in self.__opciones:
            self.__opcion_seleccionada = opcion_inicial
        elif self.__opciones:
            self.__opcion_seleccionada = self.__opciones[0]  # Seleccionar la primera por defecto
        else:
            print("Advertencia: No se proporcionaron opciones.")

    def get_opcion(self):
        return self.__opcion_seleccionada

    def set_opcion(self, nueva_opcion):
        if nueva_opcion in self.__opciones:
            self.__opcion_seleccionada = nueva_opcion
            print(f"Opción seleccionada actualizada a: {self.__opcion_seleccionada}")
        else:
            print(f"Error: La opción '{nueva_opcion}' no es válida.")

    def ejecutar_accion(self):
        opcion = self.get_opcion()
        if opcion == 'Opción A': print("Ejecutando acción para Opción A...")
        elif opcion == 'Opción B':print("Ejecutando acción para Opción B...")
        elif opcion == 'Opción C': print("Ejecutando acción para Opción C...")
        elif opcion: print(f"No hay acción definida para la opción: {opcion}")
        else: print("No hay ninguna opción seleccionada.")

# Probar cada opción cambiando el valor con el setter y ejecutando la acción
opciones_selector = SelectorOpciones(['Opción A', 'Opción B', 'Opción C'], 'Opción A')

print("Opción inicial:", opciones_selector.get_opcion())
opciones_selector.ejecutar_accion()
print("-" * 20)

# Cambiar a Opción B
opciones_selector.set_opcion('Opción B')
opciones_selector.ejecutar_accion()
print("-" * 20)

# Cambiar a Opción C
opciones_selector.set_opcion('Opción C')
opciones_selector.ejecutar_accion()
print("-" * 20)

# Intentar establecer una opción no válida
opciones_selector.set_opcion('Opción D')
print("Opción actual:", opciones_selector.get_opcion())
opciones_selector.ejecutar_accion()