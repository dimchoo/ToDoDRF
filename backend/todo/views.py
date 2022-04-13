from rest_framework.viewsets import ModelViewSet
from todo.serializers import ProjectSerializer, ProjectUserSerializer, TaskStatusSerializer, TaskSerializer
from todo.models import Project, ProjectUser, TaskStatus, Task


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectUserViewSet(ModelViewSet):
    serializer_class = ProjectUserSerializer
    queryset = ProjectUser.objects.all()


class TaskStatusViewSet(ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
