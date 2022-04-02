from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
