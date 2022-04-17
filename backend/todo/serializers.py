from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from todo.models import Project, ProjectUser, TaskStatus, Task


class ProjectSerializer(ModelSerializer):
    # users = StringRelatedField(many=True)
    # tasks = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectUserSerializer(ModelSerializer):
    # project = StringRelatedField()
    # user = StringRelatedField()

    class Meta:
        model = ProjectUser
        fields = '__all__'


class TaskStatusSerializer(ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    # created_by = StringRelatedField()
    # users = ProjectUserSerializer(many=True)
    # status = TaskStatusSerializer()

    class Meta:
        model = Task
        fields = '__all__'
