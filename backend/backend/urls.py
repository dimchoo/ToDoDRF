from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views

from users.views import UserViewSet
from todo.views import ProjectViewSet, ProjectUserViewSet, TaskStatusViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    Info(
        title='ToDoDRF',
        default_version='0.1',
        description="The safest student project in the universe",
        contact=Contact(email="super@user.com"),
        license=License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny, ),
)

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('project-users', ProjectUserViewSet)
router.register('task-statuses', TaskStatusViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('api/jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.with_ui()),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
