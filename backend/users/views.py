from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import UserDRF
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [UserPermission, ]
    serializer_class = UserSerializer
    queryset = UserDRF.objects.all()
