from rest_framework import serializers
from .models import File, CustomUser
from django.contrib.auth.hashers import make_password

class FileSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = File
        fields = ['id', 'upload_date','url']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

        def validate_password(self, value: str) -> str:
            """
            Hash value passed by user.

            :param value: password of a user
            :return: a hashed version of the password
            """
            return make_password(value)