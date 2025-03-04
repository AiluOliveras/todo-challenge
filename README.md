# ToDo-List Challenge
Este proyecto fué desarrollado por Ailén Oliveras en Febrero 2025.

## Servicios disponibles
* Crear una tarea --> /tareas/crear (POST)
* Listado de tareas --> /tareas/ (GET)
* Filtrar listado de tareas --> /tareas/?descripcion=<str>&titulo=<str>&completada=<bool> (GET)
* Filtrar listado de tareas según fecha de creación --> /tareas/?created_at=<fecha yyyy-mm-dd> (GET)
* Filtrar listado de tareas según rango de fechas --> /tareas/?created_at__desde=<fecha yyyy-mm-dd>&created_at__hasta=<fecha yyyy-mm-dd> (GET)
* Marcar tarea como completa --> /tareas/<id>/marcar_completada (POST)
* Marcar tarea como incompleta --> /tareas/<id>/marcar_incompleta (POST)
* Eliminar tarea --> /tareas/<id> (DELETE)

* Obtener tokens de logueo--> /api/token/ (+ parámetros user y password en el body)

## Otras funcionalidades del sistema
* Proyecto dockerizado
* Tests unitarios e integrales (Pueden provarse con el comando: python3 manage.py test)
* Manejo de logs con accesos y errores (Se pueden visualizar en el archivo accesos_y_errores.log en la carpeta del sistema)

## Guía general de instalación
1- Crear carpeta que contenga el proyecto.
2- Crear entorno virtual y ejecutarlo.
3- Descargar proyecto desde GIT.
4- Crear base de datos, recomendado llamarle "todochallenge" para facilitar la configuración. Activar servicio mysql.
5- Configurar archivo settings.
6- Instalar requirements.txt.
7- Ejecutar proyecto.

## Otras aclaraciones
* Los archivos settings-base.py y docker-compose-base.py son plantillas para configurar el sistema. Deben modificarse incluyendo las credenciales de la base de datos locales, puertos preferidos, keys personales, etc. Previamente a definir estos datos, puede crearse una copia de estos archivos sin el "-base" para preservar la configuración elegida localmente.

---

# Invera ToDo-List Challenge (Python/Django Jr-SSr)

El propósito de esta prueba es conocer tu capacidad para crear una pequeña aplicación funcional en un límite de tiempo. A continuación, encontrarás las funciones, los requisitos y los puntos clave que debés tener en cuenta durante el desarrollo.

## Qué queremos que hagas:

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
- La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un super comité de las más grandes mentes maestras de Invera, o a un par de devs, lo que sea más fácil de conseguir.
- Podes contactarnos en caso que tengas alguna consulta.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Autenticarse
- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

## Qué evaluamos:

- Desarrollo utilizando Python, Django. No es necesario crear un Front-End, pero sí es necesario tener una API que permita cumplir con los objetivos de arriba.
- Uso de librerías y paquetes estandares que reduzcan la cantidad de código propio añadido.
- Calidad y arquitectura de código. Facilidad de lectura y mantenimiento del código. Estándares seguidos.
- [Bonus] Manejo de logs.
- [Bonus] Creación de tests (unitarias y de integración)
- [Bonus] Unificar la solución propuesta en una imagen de Docker por repositorio para poder ser ejecutada en cualquier ambiente (si aplica para full stack).

## Requerimientos de entrega:

- Hacer un fork del proyecto y pushearlo en github. Puede ser privado.
- La solución debe correr correctamente.
- El Readme debe contener todas las instrucciones para poder levantar la aplicación, en caso de ser necesario, y explicar cómo se usa.
- Disponibilidad para realizar una pequeña demo del proyecto al finalizar el challenge.
- Tiempo para la entrega: Aproximadamente 7 días.
