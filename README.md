Gestor de Turnos para Centros de Salud

Este proyecto es un sistema de gestión de turnos médicos diseñado para centros de salud. 
Permite:

✅ Registrar nuevos turnos (con validación de disponibilidad)
✅ Listar turnos existentes
✅ Modificar turnos (cambiar especialidad, fecha/hora o estado)
✅ Eliminar turnos
✅ Validar horarios (Lunes a Viernes, de 8:00 a 18:00)
✅ Persistencia de datos (almacena turnos en un archivo JSON)

Configuración del entorno virtual

# Crear entorno virtual
Termial: python -m venv venv

# Activar entorno (Windows)
Terminal .\venv\Scripts\activat

Instalar dependencias

Terminal: pip install -r requirements.txt

Crear repositorio local

# Desde la carpeta del proyecto, abrí la terminal y ejecuté:
Terminal: git init
# Crear archivos y hacer primer comit
Terminal: git add .
Terminal: git commit -m "Inicio proyecto: estructura y clases base"

Crear el repositorio en GitHub

# Ingresá a https://github.com
# Crear nuevo repositorio: gestion-turnos
# Conectar tu repositorio local con GitHub
Terminal: git remote add origin https://github.com//libelulalibre/gestion-turnos.git
Teminal: git push -u origin main

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


Ejecución del Programa

Terminal: python main.py

Sigue el menú interactivo:

--- MENÚ DE GESTIÓN DE TURNOS ---
1. Registrar turno
2. Listar turnos
3. Modificar turno
4. Eliminar turno
5. Salir



Desarrollado por: Nicolás Cárdenas
Fecha de entrega: 12/05/2025
Curso: Curso Python + FastAPI

