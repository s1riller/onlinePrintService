from django.urls import path
from .views import UploadFileAPIView, UserAPIView, UserAvatarAPIView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
urlpatterns = [

    path('file/',UploadFileAPIView.as_view(), name='api_upload_file'),

    path('',UserAPIView.as_view(), name="api_user"),
    path('avatar/',UserAvatarAPIView.as_view(), name="api_avatar_user"),


    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
