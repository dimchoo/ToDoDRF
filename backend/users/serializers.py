from rest_framework.serializers import ModelSerializer
from users.models import UserDRF


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserDRF
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'photo']
