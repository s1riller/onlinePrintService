from django.urls import path
from .views import MultiFunctionFileAPIView, UserAPIView, UserAvatarAPIView, FileDetailAPIView, RegisterUserAPIView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
urlpatterns = [

    path('file/',MultiFunctionFileAPIView.as_view(), name='api_upload_file'),
    path('file/<int:id>/',FileDetailAPIView.as_view(), name='detail_file'),

    path('',UserAPIView.as_view(), name="api_user"),
    path('avatar/',UserAvatarAPIView.as_view(), name="api_avatar_user"),


    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("register/", RegisterUserAPIView.as_view(), name="register_user"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
