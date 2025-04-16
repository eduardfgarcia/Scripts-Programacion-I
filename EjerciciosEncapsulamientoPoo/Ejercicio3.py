
# Ejercicio 3: Crear una cuenta y validar el acceso con diferentes combinaciones -
# Encapsular el usuario y la contraseña con validación mediante métodos públicos.


class Cuenta:
    contrasena: int
    def __init__(self, usuario, contrasena):
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__intentos = 1    

    def set_contraseña(self,nuevaContraseña):
        if nuevaContraseña != self.__contrasena:
            self.__contrasena = nuevaContraseña
            return 'Contraseña cambiada'
        else: return 'La nueva contraseña no puede ser igual a la anterior'
    
    def validar_acceso(self, usuario, contrasena):
        if self.__intentos <= 3:
            if usuario == self.__usuario and contrasena == self.__contrasena: return f'Acceso concedido | Intentos: {self.__intentos}'
            else:
                self.__intentos += 1
                return 'Acceso denegado'
        else: return 'Acceso bloqueado por demasiados intentos fallidos'
    
    def get_account(self):
        return f'Cuenta : {self.__usuario, self.__contrasena}'

# objetos de cuenta 

cuenta1 = Cuenta('Eduard', 1234)
cuenta2 = Cuenta('Juan', 1234)


print(cuenta1.set_contraseña(2905))
print(cuenta1.validar_acceso('Eduard', 1234)) # Acceso denegado
print(cuenta1.validar_acceso('Eduard', 2905)) # Acceso concedido
print(cuenta1.get_account())

