from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from todochallengeApp.views import TareasList, TareasDelete, MarcarTareaCompletadaView, MarcarTareaIncompletaView, TareasCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    #Servicios
    path('tareas/', TareasList.as_view(), name='tareas_list'),
    path('tareas/crear', TareasCreate.as_view(), name='tareas_create'),
    path('tareas/<int:pk>', TareasDelete.as_view(), name='tareas_delete'),
    path('tareas/<int:pk>/marcar_completada', MarcarTareaCompletadaView.as_view(), name='marcar_tarea_completada'),
    path('tareas/<int:pk>/marcar_incompleta', MarcarTareaIncompletaView.as_view(), name='marcar_tarea_incompleta'),

    #Autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
