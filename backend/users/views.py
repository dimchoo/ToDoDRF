from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import UserDRF
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserSerializerV2


class UserViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [UserPermission, ]
    # serializer_class = UserSerializer
    queryset = UserDRF.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserSerializerV2
        return UserSerializer
