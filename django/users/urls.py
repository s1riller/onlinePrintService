from django.urls import path

from .views import RegistrationAPIView,LoginAPIView, UserRetrieveUpdateAPIView
app_name = 'authentication'
urlpatterns = [
    path('retrieveUpdate/', UserRetrieveUpdateAPIView.as_view()),
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]