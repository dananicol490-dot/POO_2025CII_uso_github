class Persona:
    '''
    Clase que permite crear un objeto de tipo Persona
    '''
    def __init__(self, cedula:str, nombre:str, email:str, genero:str = None
                 , ocupacion:str = None, edad:int = None):
        self._cedula = cedula
        self._email = email
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._edad = edad
        self._activo = True

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nueva_nombre):
        self._nombre = nueva_nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nueva_email):
        self._email = nueva_email

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nueva_genero):
        self._genero = nueva_genero

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, nueva_ocupacion):
        self._ocupacion = nueva_ocupacion

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def activo(self):
        return self._activo

    # @activo.setter
    # def activo(self, nueva_activo):
    #     self._activo = nueva_activo

    def inactivar_persona(self):
        self._activo = False

    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'

if __name__ == '__main__':
    # persona1 = {"nombre":"Carlos", "ocupacion":"Estudiante"}
    # print(persona1["nombre"])
    # print(type(persona1))
    #
    # print("*".center(80, "*"))
    #
    # persona2 = Persona(nombre = 'Carlos Perez', genero = 'H', ocupacion='Estudiante', edad=20,
    #                    cedula = '0987654312', email = 'cperez@mail.com', )
    # print(persona2._nombre)
    #
    # print(type(persona2))
    # print(f'Nombre: {persona2._nombre}')
    # print(f'Cedula: {persona2._cedula}')
    # print(f'Email: {persona2._email}')
    # print(f'Ocupacion: {persona2._ocupacion}')
    #
    # print("*".center(80, "*"))
    #
    # persona4 = Persona('0987654321', 'Maria Perez', 'mperez@mail.com',
    #                    'M', 'Doctora', 30)
    # print(f'Nombre: {persona4._nombre}')
    # print(f'Cedula: {persona4._cedula}')
    # print(f'Email: {persona4._email}')
    # print(f'Ocupacion: {persona4._ocupacion}')
    #
    # print("*".center(80, "*"))
    #
    # persona5 = Persona(nombre='Luis Paz', genero = 'H', ocupacion='Ingeniero'
    #                    , edad='Veinticinco',
    #                    cedula = 1987654314, email = 'lperez@mail.com')
    # print(f'Nombre: {persona5._nombre}')
    # print(f'Cedula: {persona5._cedula}')
    # print(f'Email: {persona5._email}')
    # print(f'Ocupacion: {persona5._ocupacion}')
    # print(f'Edad: {persona5._edad}')
    objPersona1 = Persona(cedula='0123456789', nombre='Luis Perez', email='lperez@mail.com',)
    # print(objPersona1._cedula)
    # objPersona1._cedula = '9876543210'
    # print(objPersona1._cedula)
    print(objPersona1.cedula)
    objPersona1.cedula = '9876543210'
    print(objPersona1.cedula)
    objPersona1.inactivar_persona()
    print(objPersona1.activo)
    print(objPersona1)

    objPersona2 = Persona(cedula='8976541230', nombre = 'Maria Paz', email='mpaz@mail.com')
    print(objPersona2.cedula)
    objPersona2.cedula = '1111111111'
    print(objPersona2.cedula)
    print(objPersona2.__str__())