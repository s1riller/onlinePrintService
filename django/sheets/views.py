from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PepperFormat
from .serializers import PepperFormatSerializer

class PepperFormatViewSet(viewsets.ModelViewSet):
    queryset = PepperFormat.objects.all()
    serializer_class = PepperFormatSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


