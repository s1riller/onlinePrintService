from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PepperFormatViewSet

# router = DefaultRouter()
# router.register(r'pepper-formats', PepperFormatViewSet)

urlpatterns = [
    path('pepper-formats/', PepperFormatViewSet.as_view({'get': 'list'})),
]
