from django.test import TestCase, Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from ..models import Tareas


class MarcarTareaCompletadaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='usuariotest', password='password')
        self.tarea = Tareas.objects.create(
            titulo='Prueba Tarea Completada',
            descripcion='Esta es una descripción'
        )

        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_marcar_tarea_completada(self):
        #Verificamos que la tarea inicialmente no está completada
        self.assertFalse(self.tarea.completada)

        #Hacemos un POST para marcar la tarea como completada
        url = reverse('marcar_tarea_completada', kwargs={'pk': self.tarea.pk})
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')

        #Recargamos la tarea desde la bbdd
        self.tarea.refresh_from_db()

        #Verificamos que la tarea ahora este completada
        self.assertTrue(self.tarea.completada)

        #Verificamos que la vista retorna código 200
        self.assertEqual(response.status_code, 200)