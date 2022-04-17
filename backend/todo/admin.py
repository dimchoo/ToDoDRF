from django.contrib import admin
from todo.models import Project, ProjectUser, TaskStatus, Task


admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(TaskStatus)
admin.site.register(Task)
