from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileSerializer, CustomUserSerializer,RegisterSerializer
import requests
from users.models import CustomUser
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import File, UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

load_dotenv()

url = os.getenv("NEXTCLOUD_URL")
nextcloud_admin_user = os.getenv("NEXTCLOUD_ADMIN_USER")
nextcloud_admin_password = os.getenv("NEXTCLOUD_ADMIN_PASSWORD")


class MultiFunctionFileAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userid = CustomUserSerializer(request.user).data['id']

        user_files = File.objects.filter(owner=userid)

        file_serializer = FileSerializer(user_files, many=True)
        response_data = {
            "files": file_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            file = request.FILES['file']
            file_content = file.read()

            username = CustomUser.objects.get(id=CustomUserSerializer(request.user).data['id']).username

            folder_url = f"http://{url}/remote.php/webdav/{username}/"

            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_with_time = f"{current_time}_{file.name}"
            upload_url = f"{folder_url}{filename_with_time}"

            # Попытка создать папку, если она не существует
            folder_response = requests.request("MKCOL", folder_url,
                                               auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))

            # Загрузка файла
            file_response = requests.put(upload_url, data=file_content,
                                         auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))

            if file_response.status_code in [200, 201]:
                file_serializer.save(owner=CustomUser.objects.get(id=CustomUserSerializer(request.user).data['id']))
                file_instance = file_serializer.instance
                file_instance.name = filename_with_time
                file_instance.url = upload_url
                file_instance.save()

                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_response.text, status=file_response.status_code)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        file_id = request.data.get('file_id')

        if not file_id:
            return Response("File ID is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            file = File.objects.get(id=file_id)
            file.delete()
            return Response("File deleted", status=status.HTTP_204_NO_CONTENT)
        except File.DoesNotExist:
            return Response("File not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Ловим и сообщаем о любых других ошибках, возникших в процессе
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FileDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        try:
            file = File.objects.get(id=id, owner=request.user)  # Ensure the file belongs to the logged-in user
            serializer = FileSerializer(file)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

#Не работает
    def delete(self, request, id, *args, **kwargs):
        try:
            file = File.objects.get(id=id, owner=request.user)
            file.delete()
            return Response({'message': 'File deleted'}, status=status.HTTP_204_NO_CONTENT)
        except File.DoesNotExist:
            return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = CustomUserSerializer(CustomUser.objects.all(), many=True)

        return Response(response.data, status=status.HTTP_200_OK)


class UserAvatarAPIView(APIView):
    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file = request.FILES['file']
            file_content = file.read()
            file_serializer.save(owner=request.user)

            username = CustomUser.objects.get(id=CustomUserSerializer(request.user).data['id']).username
            folder_url = f"http://{url}/remote.php/webdav/{username}/"

            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename_with_time = f"{current_time}_{file.name}"

            # Попытка создать папку, если она не существует
            folder_response = requests.request("MKCOL", folder_url,
                                               auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))
            folder_url = f"http://{url}/remote.php/webdav/{username}/avatar/"

            folder_response = requests.request("MKCOL", folder_url,
                                               auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))
            upload_url = f"{folder_url}{filename_with_time}"
            # Загрузка файла
            file_response = requests.put(upload_url, data=file_content,
                                         auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))

            if file_response.status_code in [200, 201]:


                file_instance = file_serializer.instance
                file_instance.name = filename_with_time
                file_instance.url = upload_url
                file_instance.save()

                User.objects.update_or_create(
                    user=request.user,
                    defaults={'avatar': file_instance}
                )

                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_response.text, status=file_response.status_code)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        def get(self, request, id, *args, **kwargs):
            try:
                file = File.objects.get(id=id, owner=request.user)  # Ensure the file belongs to the logged-in user
                serializer = FileSerializer(file)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except File.DoesNotExist:
                return Response({'message': 'Avatar not found'}, status=status.HTTP_404_NOT_FOUND)


class RegisterUserAPIView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
