from rest_framework import serializers
from .models import PepperFormat

class PepperFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PepperFormat
        fields = '__all__'