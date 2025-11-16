from persona import Persona


class Cliente(Persona):
    """
    Clase que hereda de Persona para crear un objeto de tipo Cliente
    """

    def __init__(self, id: int, sueldo: float, nombre: str, email: str,
                 genero: str, edad: int, ocupacion: str, cedula: str,
                 fecha_registro: str, tipo_cliente: str):

        # Llamar al constructor de la clase padre (Persona)
        super().__init__(nombre=nombre, email=email, genero=genero,
                         edad=edad, ocupacion=ocupacion, cedula=cedula)

        self._id = id
        self._sueldo = sueldo
        self._fecha_registro = fecha_registro
        self._tipo_cliente = tipo_cliente

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, nueva_fecha):
        self._fecha_registro = nueva_fecha

    @property
    def tipo_cliente(self):
        return self._tipo_cliente

    @tipo_cliente.setter
    def tipo_cliente(self, nuevo_tipo):
        self._tipo_cliente = nuevo_tipo

    def __str__(self):
        return (f'{super().__str__()}, ID: {self._id}, Sueldo: {self._sueldo}, '
                f'Fecha Registro: {self._fecha_registro}, Tipo: {self._tipo_cliente}')


if __name__ == "__main__":
    objCliente1 = Cliente(id=1, nombre='Dana Rodriguez', email='dananicol490@gmail.com',
                          genero='F', ocupacion='abogada', edad=22,
                          cedula='0996491766', sueldo=1800,
                          fecha_registro='2025-11-26', tipo_cliente='Premium')

    print(objCliente1)
    print('*' * 80)
    print(f"Nombre: {objCliente1.nombre}")
    print(f"Email: {objCliente1.email}")
    print(f"Tipo de Cliente: {objCliente1.tipo_cliente}")
    print(f"Sueldo: ${objCliente1.sueldo}")