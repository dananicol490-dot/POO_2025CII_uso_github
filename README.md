┌─────────────────────────────────┐
│          <<Motor>>              │
├─────────────────────────────────┤
│ - _tipo: str                    │
│ - _potencia: int                │
│ - _encendido: bool              │
├─────────────────────────────────┤
│ + tipo: property                │
│ + potencia: property            │
│ + encender_motor(): str         │
│ + detener_motor(): str          │
│ + acelerar(): str               │
│ + estado_motor(): str           │
│ + __str__(): str                │
└─────────────────────────────────┘
                 ▲
                 │ composición
                 │
                 │
┌─────────────────────────────────┐
│        <<Vehiculo>>             │
├─────────────────────────────────┤
│ - _marca: str                   │
│ - _modelo: str                  │
│ - _anio: int                    │
│ - _encendido: bool              │
├─────────────────────────────────┤
│ + marca: property               │
│ + modelo: property              │
│ + anio: property                │
│ + encender(): str               │
│ + apagar(): str                 │
│ + obtener_info_basica(): str    │
│ + __str__(): str                │
└─────────────────────────────────┘
                 ▲
                 │ herencia
        ┌────────┴────────┐
        │                 │
┌───────────────┐  ┌──────────────┐
│  <<Automovil>> │  │<<Motocicleta>>│
├───────────────┤  ├──────────────┤
│- _num_puertas │  │- _cilindraje │
│- _motor: Motor│  │- _motor:Motor│
│- _maletero    │  │- _caballito  │
├───────────────┤  ├──────────────┤
│+ num_puertas  │  │+ cilindraje  │
│+ motor        │  │+ motor       │
│+ abrir_male() │  │+ hacer_cab() │
│+ cerrar_male()│  │+ terminar()  │
│+ tocar_clax() │  │+ usar_patada│
│+ activar_ac() │  │+ acelerar()  │
│+ __str__()    │  │+ __str__()   │
└───────────────┘  └──────────────┘
