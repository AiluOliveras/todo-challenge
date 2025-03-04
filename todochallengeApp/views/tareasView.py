from django.test import TestCase
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, ListAPIView

from ..models import Tareas
from ..serializers import TareasSerializer
from ..filters import TareasFilter

class TareasList(ListAPIView):

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    filterset_class = TareasFilter

    permission_classes = [IsAuthenticated]


class TareasCreate(CreateAPIView):

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    
    permission_classes = [IsAuthenticated]


class TareasDelete(DestroyAPIView):

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    permission_classes = [IsAuthenticated]


class MarcarTareaCompletadaView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            tarea = Tareas.objects.get(id=pk)
            tarea.completada = True
            tarea.save()
            return Response({'message': 'Tarea marcada como: Completada'}, status=status.HTTP_200_OK)
        except Tareas.DoesNotExist:
            return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)


class MarcarTareaIncompletaView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            tarea = Tareas.objects.get(id=pk)
            tarea.completada = False
            tarea.save()
            return Response({'message': 'Tarea marcada como: Incompleta'}, status=status.HTTP_200_OK)
        except Tareas.DoesNotExist:
            return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
