import django_filters
from todo.models import Task, Project


class TaskFilter(django_filters.FilterSet):
    created_gt = django_filters.DateTimeFilter(field_name='created', lookup_expr='gt')
    created_lt = django_filters.DateTimeFilter(field_name='created', lookup_expr='lt')

    class Meta:
        model = Task
        fields = ['created', ]


class ProjectFilter(django_filters.FilterSet):
    name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['name_icontains', ]

