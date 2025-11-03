# Examen-2-parcial-Arquitectura-de-Computadoras

# Monitor del Sistema con Django + psutil

## Descripción del Proyecto

Este es un **monitor web en tiempo real** que muestra el estado actual del sistema operativo usando *Platform, Django y psutil*.

### Características principales:
- **Uso del CPU** (% y núcleos)
- **Memoria RAM** (total, usada, libre, porcentaje)
- **Disco duro** (total, usado, libre, porcentaje)
- **Información del SO** (nombre, versión, arquitectura)
- **Actualización automática cada 5 segundos** (sin recargar la página)
- **Botón manual "Actualizar Ahora"**
- Diseño moderno con tarjetas animadas, barras de progreso y colores
- **API JSON** en `/data/` para actualizaciones dinámicas
- **Manejo de errores** (no se cae si falla algo)
  
- **Integrantes del equipo**
-  - Ingris Gissel Samayoa 202310010702
-  - Yudith Skarleth Rodriguez Mejia 201330060004

> Ideal para monitorear el rendimiento del sistema local desde el navegador.

## Instrucciones para Ejecutar Localmente con Visual Studio Code
- Abrir la carpeta del archivo/proyecto
- abrir la terminal integrada en VSC
  
-Crear o activar el entorno virtual con el comando:
----Crear -->> python -m venv venv
----Activar -->> venv\Scripts\activate
  
-Instalar las dependencias
----pip install -r requirements.txt

-Aplicar migraciones
----python manage.py migrate

-Inicializar el servidor
----python manage.py runserver
--Mostrará una ruta o link, dar clic sobre el y alli nos cargará la pantalla en el navegador con el monitor actualizandose en tiempo real

-Detener el servidor
----En la terminal de Visual Studio Code colocamos la combinacion de teclas: Control + C

**Instalacion de dependencias**

--Archivo: requirements.txt
      Django: Framework web: vistas, rutas, plantillas, servidor de desarrollo
      Psutil: Libreria multiplataforma que sirve para obtener metricas del sistema       como la CPU, RAM, Disco
Se instalan con un solo comando: pip install -r requirements.txt

**1. Archivo: views.py**
  Logica principal:
  
def get_system_info():
    # Recolecta todos los datos del sistema con psutil
    # Convierte bytes → GB
    # Maneja errores con try/except
    return diccionario_con_datos

Recoleccion de datos:

  import psutil
  import platform

  cpu = psutil.cpu_percent(interval=1)
  mem = psutil.virtual_memory()
  disk = psutil.disk_usage('C:/') 

--utiliza psutil para consultarle al sistema

**2. Interfaz web: archivo: principal.html**

fetch('/data/') → recibe JSON → actualiza tarjetas
refresca automaticamente cada 5 segundos
boton para refrescar manualmente

**3. Rutas: archivo: urls.py**

path('', views.index)  --> Página principal
path('data/', views.system_data) --> API JSON
