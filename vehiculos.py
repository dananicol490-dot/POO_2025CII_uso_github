import re

class Vehiculo:
    def __init__(self, marca, modelo, placa):
        self._marca = marca
        self._modelo = modelo
        self.placa = placa  # Se valida más adelante con el setter

    # Propiedad para marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca

    # Propiedad para modelo
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    # Propiedad para placa con validación
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, nueva_placa):
        if isinstance(nueva_placa, str) and re.fullmatch(r'[A-Z]{3}\d{4}', nueva_placa.upper()):
            self._placa = nueva_placa.upper()
        else:
            raise ValueError("La placa debe tener 3 letras seguidas de 4 números (ej. ABC1234)")

    # Método para mostrar la información
    def __str__(self):
        return f"Vehiculo: {self.__dict__.__str__()}"

if __name__ == '__main__':
    objVehiculo1 = Vehiculo(marca='Ford', modelo='Mustang', placa='POI9634')
    print(objVehiculo1)
    objVehiculo1.placa = 'GTR1234'
    # objVehiculo1._placa = 'GTR1234'
    print(objVehiculo1)
    print(objVehiculo1)