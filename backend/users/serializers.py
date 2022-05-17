from rest_framework.serializers import ModelSerializer
from users.models import UserDRF


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserDRF
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'photo']


class UserSerializerV2(ModelSerializer):
    class Meta:
        model = UserDRF
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'photo',
            'is_superuser',
            'is_staff'
        ]

