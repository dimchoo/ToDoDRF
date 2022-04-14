import django_filters
from todo.models import Task


class TaskFilter(django_filters.FilterSet):
    created_gt = django_filters.DateFilter(field_name='created', lookup_expr='gt')
    created_lt = django_filters.DateFilter(field_name='created', lookup_expr='lt')

    class Meta:
        model = Task
        fields = ['created', ]

