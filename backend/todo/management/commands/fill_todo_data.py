from django.core.management.base import BaseCommand
from django.conf import settings
import os
import random
import json
from users.models import UserDRF
from todo.models import Project, ProjectUser, TaskStatus, Task


class Command(BaseCommand):
    def handle(self, *args, **options):
        json_path = os.path.join(settings.BASE_DIR, 'todo_data.json')
        all_users = UserDRF.objects.all()
        with open(json_path, encoding='UTF-8') as file:
            todo_data = json.load(file)
            projects = todo_data.get('projects')
            task_statuses = todo_data.get('task_statuses')
            tasks = todo_data.get('tasks')

        Project.objects.bulk_create(
            [Project(**i, created_by=random.choice(all_users)) for i in projects]
        )
        projects = Project.objects.all()
        ProjectUser.objects.bulk_create(
            [ProjectUser(project=random.choice(projects), user=u) for u in all_users]
        )
        TaskStatus.objects.bulk_create(
            [TaskStatus(**i) for i in task_statuses]
        )
        statuses = TaskStatus.objects.all()
        Task.objects.bulk_create(
            [Task(**i, project=random.choice(projects), status=random.choice(statuses)) for i in tasks]
        )
        tasks = Task.objects.all()
        for obj in tasks.iterator():
            users = ProjectUser.objects.filter(project=obj.project)
            print(users)
            obj.created_by = random.choice(all_users)
            obj.users.set(users)
            obj.save()

