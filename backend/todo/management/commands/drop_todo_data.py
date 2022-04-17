from django.core.management.base import BaseCommand
from todo.models import Project, ProjectUser, TaskStatus, Task


class Command(BaseCommand):
    def handle(self, *args, **options):
        Project.objects.all().delete()
        ProjectUser.objects.all().delete()
        TaskStatus.objects.all().delete()
        Task.objects.all().delete()