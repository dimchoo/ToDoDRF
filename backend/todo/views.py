from rest_framework.viewsets import ModelViewSet
from todo.serializers import ProjectSerializer, ProjectUserSerializer, TaskStatusSerializer, TaskSerializer
from todo.models import Project, ProjectUser, TaskStatus, Task
from todo.paginators import ProjectPaginator, TaskPaginator
from todo.permissions import ProjectPermission, TaskPermission
import django_filters
from todo.filters import TaskFilter


class ProjectViewSet(ModelViewSet):
    # pagination_class = ProjectPaginator
    # permission_classes = [ProjectPermission, ]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Project.objects.filter(name__icontains=name)
        return Project.objects.all()


class ProjectUserViewSet(ModelViewSet):
    serializer_class = ProjectUserSerializer
    queryset = ProjectUser.objects.all()


class TaskStatusViewSet(ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()


class TaskViewSet(ModelViewSet):
    permission_classes = [TaskPermission, ]
    filter_class = TaskFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    # pagination_class = TaskPaginator
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(is_active=True)

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name', None)
        if project_name:
            return Task.objects.filter(project__name__iexact=project_name)
        return Task.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
