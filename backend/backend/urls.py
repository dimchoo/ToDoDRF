from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet
from todo.views import ProjectViewSet, ProjectUserViewSet, TaskStatusViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('project-users', ProjectUserViewSet)
router.register('task-statuses', TaskStatusViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
