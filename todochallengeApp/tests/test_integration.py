from django.test import TestCase, Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from ..models import Tareas


class IntegracionTareasTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='usuariotestintegrador', password='password')
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_crear_y_marcar_tarea_completada(self):
        #Generamos token
        auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

        #Creamos una tarea
        url_crear = reverse('tareas_create')
        datos_tarea = {
            'titulo': 'Tarea de integración',
            'descripcion': 'Esta es una tarea de prueba para integración'
        }
        response_crear = self.client.post(url_crear, datos_tarea, **auth_header)
        self.assertEqual(response_crear.status_code, 201) #Verifica recibir respuesta http 201

        #Busca la tarea creada en la bbdd
        tarea_id = response_crear.json().get('id')
        tarea = Tareas.objects.get(id=tarea_id)

        #Verifica que no esté completada
        self.assertFalse(tarea.completada)

        #Marcamos la tarea como completada
        url_marcar = reverse('marcar_tarea_completada', kwargs={'pk': tarea.pk})
        response_marcar = self.client.post(url_marcar, **auth_header)
        self.assertEqual(response_marcar.status_code, 200) #Verifica recibir respuesta http 200

        #Recargamos la tarea desde la bbdd
        tarea.refresh_from_db()
        self.assertTrue(tarea.completada)