from rest_framework.viewsets import ModelViewSet
from users.models import UserDRF
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserDRF.objects.all()
