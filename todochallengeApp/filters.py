from .models import Tareas
import django_filters

class TareasFilter(django_filters.FilterSet):

    titulo = django_filters.CharFilter(field_name='titulo', lookup_expr='icontains')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    completada = django_filters.BooleanFilter(field_name='completada')
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='icontains')
    
    created_at__desde = django_filters.DateFilter(field_name='created_at', lookup_expr='gt')
    created_at__hasta = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')

    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'completada','created_at','created_at__desde','created_at__hasta']
