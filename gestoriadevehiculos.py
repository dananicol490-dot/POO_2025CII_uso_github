"""
Sistema de Gestión de Vehículos
Implementa: Herencia, Composición, Encapsulamiento y Métodos de Comportamiento
"""


class Motor:
    """Clase Motor - Utilizada para composición"""

    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia
        self._encendido = False

    # Getters y Setters con @property
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, valor):
        if valor > 0:
            self._potencia = valor
        else:
            raise ValueError("La potencia debe ser mayor a 0")

    # Métodos de comportamiento
    def encender_motor(self):
        if not self._encendido:
            self._encendido = True
            return f"Motor {self._tipo} de {self._potencia} HP encendido"
        return " El motor ya está encendido"

    def detener_motor(self):
        if self._encendido:
            self._encendido = False
            return f" Motor {self._tipo} detenido"
        return "  El motor ya está apagado"

    def acelerar(self):
        if self._encendido:
            return f" ¡VROOOOM! Motor acelerando a {self._potencia} HP"
        return "  Debes encender el motor primero"

    def estado_motor(self):
        estado = "encendido" if self._encendido else "apagado"
        return f"Motor: {estado}"

    def __str__(self):
        estado = "encendido" if self._encendido else "apagado"
        return f"Motor {self._tipo} - {self._potencia} HP ({estado})"


class Vehiculo:
    """Superclase Vehiculo - Clase base para todos los vehículos"""

    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._encendido = False

    # Getters y Setters con @property
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if 1900 <= valor <= 2025:
            self._anio = valor
        else:
            raise ValueError("Año inválido")

    # Métodos de comportamiento
    def encender(self):
        if not self._encendido:
            self._encendido = True
            return f" {self._marca} {self._modelo} encendido"
        return "  El vehículo ya está encendido"

    def apagar(self):
        if self._encendido:
            self._encendido = False
            return f" {self._marca} {self._modelo} apagado"
        return "  El vehículo ya está apagado"

    def obtener_info_basica(self):
        return f"{self._marca} {self._modelo} ({self._anio})"

    def __str__(self):
        estado = "encendido" if self._encendido else "apagado"
        return f"Vehículo: {self._marca} {self._modelo} - Año: {self._anio} - Estado: {estado}"


class Automovil(Vehiculo):
    """Clase Automovil - Hereda de Vehiculo"""

    def __init__(self, marca, modelo, anio, num_puertas, motor):
        super().__init__(marca, modelo, anio)
        self._num_puertas = num_puertas
        self._motor = motor  # Composición
        self._maletero_abierto = False

    @property
    def num_puertas(self):
        return self._num_puertas

    @num_puertas.setter
    def num_puertas(self, valor):
        if valor in [2, 3, 4, 5]:
            self._num_puertas = valor
        else:
            raise ValueError("Número de puertas inválido")

    @property
    def motor(self):
        return self._motor

    # Métodos de comportamiento
    def abrir_maletero(self):
        if not self._maletero_abierto:
            self._maletero_abierto = True
            return " Maletero abierto"
        return "️  El maletero ya está abierto"

    def cerrar_maletero(self):
        if self._maletero_abierto:
            self._maletero_abierto = False
            return " Maletero cerrado"
        return "️  El maletero ya está cerrado"

    def tocar_claxon(self):
        return " ¡BEEP BEEP! "

    def activar_aire_acondicionado(self):
        if self._encendido:
            return "️  Aire acondicionado activado"
        return "  Enciende el automóvil primero"

    def __str__(self):
        base = super().__str__()
        maletero = "abierto" if self._maletero_abierto else "cerrado"
        return (f"{base}\n"
                f"  Tipo: Automóvil - Puertas: {self._num_puertas}\n"
                f"  {self._motor}\n"
                f"  Maletero: {maletero}")


class Motocicleta(Vehiculo):
    """Clase Motocicleta - Hereda de Vehiculo"""

    def __init__(self, marca, modelo, anio, cilindraje, motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self._motor = motor  # Composición
        self._caballito_activo = False

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        if valor > 0:
            self._cilindraje = valor
        else:
            raise ValueError("El cilindraje debe ser mayor a 0")

    @property
    def motor(self):
        return self._motor

    # Métodos de comportamiento
    def hacer_caballito(self):
        if self._encendido and not self._caballito_activo:
            self._caballito_activo = True
            return "  ¡Haciendo un caballito! ¡WOOO! "
        elif not self._encendido:
            return "️  Enciende la motocicleta primero"
        return "  Ya estás haciendo un caballito"

    def terminar_caballito(self):
        if self._caballito_activo:
            self._caballito_activo = False
            return " Caballito terminado, rueda delantera en el suelo"
        return "  No estás haciendo un caballito"

    def usar_patada_arranque(self):
        if not self._encendido:
            return " ¡Patada de arranque! *KICK* - Motor listo"
        return "  La motocicleta ya está encendida"

    def acelerar_rapido(self):
        if self._encendido:
            return f" ¡Acelerando a fondo! {self._cilindraje}cc rugiendo"
        return " Enciende la motocicleta primero"

    def __str__(self):
        base = super().__str__()
        caballito = "haciendo caballito" if self._caballito_activo else "normal"
        return (f"{base}\n"
                f"  Tipo: Motocicleta - Cilindraje: {self._cilindraje}cc\n"
                f"  {self._motor}\n"
                f"  Posición: {caballito}")


# ===== PROGRAMA PRINCIPAL =====
def main():
    print("=" * 70)
    print("SISTEMA DE GESTIÓN DE VEHÍCULOS - POO EN PYTHON ️")
    print("=" * 70)
    print()

    # Crear motores
    motor1 = Motor("V8 Biturbo", 450)
    motor2 = Motor("V6", 300)
    motor3 = Motor("Monocilíndrico", 25)
    motor4 = Motor("Bicilíndrico", 150)

    # Crear automóviles
    print(" CREANDO AUTOMÓVILES...\n")
    auto1 = Automovil("Toyota", "Camry", 2023, 4, motor1)
    auto2 = Automovil("Honda", "Civic", 2022, 4, motor2)

    # Crear motocicletas
    print("CREANDO MOTOCICLETAS...\n")
    moto1 = Motocicleta("Yamaha", "YZF-R3", 2023, 321, motor3)
    moto2 = Motocicleta("Kawasaki", "Ninja 650", 2024, 649, motor4)

    print("=" * 70)
    print(" PRUEBA DE AUTOMÓVIL 1: Toyota Camry")
    print("=" * 70)
    print(auto1)
    print()
    print(auto1.encender())
    print(auto1.motor.encender_motor())
    print(auto1.tocar_claxon())
    print(auto1.abrir_maletero())
    print(auto1.motor.acelerar())
    print(auto1.activar_aire_acondicionado())
    print()

    print("=" * 70)
    print("PRUEBA DE AUTOMÓVIL 2: Honda Civic")
    print("=" * 70)
    print(auto2)
    print()
    print(auto2.encender())
    print(auto2.motor.encender_motor())
    print(auto2.tocar_claxon())
    print(auto2.abrir_maletero())
    print(auto2.cerrar_maletero())
    print()

    print("=" * 70)
    print("  PRUEBA DE MOTOCICLETA 1: Yamaha YZF-R3")
    print("=" * 70)
    print(moto1)
    print()
    print(moto1.usar_patada_arranque())
    print(moto1.encender())
    print(moto1.motor.encender_motor())
    print(moto1.hacer_caballito())
    print(moto1.acelerar_rapido())
    print(moto1.terminar_caballito())
    print()

    print("=" * 70)
    print(" PRUEBA DE MOTOCICLETA 2: Kawasaki Ninja 650")
    print("=" * 70)
    print(moto2)
    print()
    print(moto2.encender())
    print(moto2.motor.encender_motor())
    print(moto2.hacer_caballito())
    print(moto2.motor.acelerar())
    print()

    print("=" * 70)
    print(" ESTADO FINAL DE TODOS LOS VEHÍCULOS")
    print("=" * 70)
    print("\n AUTOMÓVILES:")
    print("-" * 70)
    print(auto1)
    print()
    print(auto2)
    print()

    print("\n  MOTOCICLETAS:")
    print("-" * 70)
    print(moto1)
    print()
    print(moto2)
    print()

    # Apagar vehículos
    print("=" * 70)
    print(" APAGANDO TODOS LOS VEHÍCULOS...")
    print("=" * 70)
    print(auto1.apagar())
    print(auto1.motor.detener_motor())
    print(auto2.apagar())
    print(auto2.motor.detener_motor())
    print(moto1.apagar())
    print(moto1.motor.detener_motor())
    print(moto2.apagar())
    print(moto2.motor.detener_motor())
    print()

    print("=" * 70)
    print(" PROGRAMA FINALIZADO")
    print("=" * 70)


if __name__ == "__main__":
    main()