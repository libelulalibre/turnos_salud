Gestor de Turnos para Centros de Salud

Descripción del Proyecto

Este proyecto es un sistema de gestión de turnos médicos diseñado para centros de salud. 
Permite:

✅ Registrar nuevos turnos (con validación de disponibilidad)
✅ Listar turnos existentes
✅ Modificar turnos (cambiar especialidad, fecha/hora o estado)
✅ Eliminar turnos
✅ Validar horarios (Lunes a Viernes, de 8:00 a 18:00)
✅ Persistencia de datos (almacena turnos en un archivo JSON)

turnos_salud/
├── data/
│   └── turnos.json          # Base de datos de turnos (se crea automáticamente)
├── controllers/
│   └── gestor_turnos.py     # Lógica principal (registro, validación, etc.)
├── models/
│   ├── turno.py             # Clase Turno (estructura de datos)
│   └── paciente.py          # Clase Paciente (opcional, no usada en versión final)
├── main.py                  # Punto de entrada del programa
├── README.md                # Este archivo
└── requirements.txt         # Dependencias (vacío o con librerías adicionales)