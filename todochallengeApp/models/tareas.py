from django.db import models

class Tareas(models.Model):
    """
    Representa una tarea de desarrollo pendiente.

    Atributos:
        titulo: String nombre de la tarea.
        descripcion: String especificación de la tarea a realizar.
        completada: Boolean indica si la tarea fué resuelta. 
    
    """

    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=254)
    completada = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)