from django.test import TestCase
from ..models import Tareas


class TareasModelTest(TestCase):

    def setUp(self):
        self.tarea = Tareas.objects.create(
            titulo='Prueba Tarea',
            descripcion='Esta es una descripción'
        )

    def test_tarea_create(self):
        tarea = self.tarea

        #Verificamos si es instancia de la clase Tareas
        self.assertTrue(isinstance(tarea, Tareas))

        #Verificamos que se asignaron correctamente sus atributos
        self.assertEqual(tarea.titulo, 'Prueba Tarea')
        self.assertEqual(tarea.descripcion, 'Esta es una descripción')
        self.assertFalse(tarea.completada)
        self.assertIsNotNone(tarea.created_at)