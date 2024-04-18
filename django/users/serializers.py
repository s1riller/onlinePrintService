from rest_framework import serializers
from .models import File, CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class FileSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = File
        fields = ['id', 'upload_date','url','owner']


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

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ( 'password', 'password2', 'email', 'first_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            # username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )


        user.set_password(validated_data['password'])
        user.save()

        return user

