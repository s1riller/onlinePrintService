import requests
from requests.auth import HTTPBasicAuth


from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("NEXTCLOUD_URL")
nextcloud_admin_user = os.getenv("NEXTCLOUD_ADMIN_USER")
nextcloud_admin_password = os.getenv("NEXTCLOUD_ADMIN_PASSWORD")


def create_user(userid, password):
    auth_url = f'http://{nextcloud_admin_user}:{nextcloud_admin_password}@{url}/ocs/v1.php/cloud/users'
    auth = HTTPBasicAuth(os.getenv("NEXTCLOUD_ADMIN_USER"), os.getenv("NEXTCLOUD_ADMIN_PASSWORD"))
    headers = {
        "OCS-APIRequest": "true"
    }
    data = {
        "userid": userid,
        "password": password
    }

    response = requests.post(auth_url, auth=auth, headers=headers, data=data)
    if response.status_code == 200:
        print("Пользователь успешно создан")
        print(response)
    else:
        print(f"Ошибка при создании пользователя: {response.status_code} {response.text}")

    return response.text


def delete_user(userid):
    delete_url = f'http://{nextcloud_admin_user}:{nextcloud_admin_password}@{url}/ocs/v1.php/cloud/users/{userid}'
    auth = HTTPBasicAuth(os.getenv("NEXTCLOUD_ADMIN_USER"), os.getenv("NEXTCLOUD_ADMIN_PASSWORD"))
    headers = {
        "OCS-APIRequest": "true"
    }
    data = {
        "userid": userid,
    }

    response = requests.delete(delete_url, auth=auth, headers=headers, data=data)
    if response.status_code == 200:
        print("Пользователь успешно удален")
        print(response)
    else:
        print(f"Ошибка при удалении пользователя: {response.status_code} {response.text}")

    return response.text

def disable_user(userid):
    disable_url = f'http://{nextcloud_admin_user}:{nextcloud_admin_password}@{url}/ocs/v1.php/cloud/users/{userid}/disable'
    auth = HTTPBasicAuth(os.getenv("NEXTCLOUD_ADMIN_USER"), os.getenv("NEXTCLOUD_ADMIN_PASSWORD"))
    headers = {
        "OCS-APIRequest": "true"
    }
    data = {
        "userid": userid,
    }

    response = requests.put(disable_url, auth=auth, headers=headers, data=data)
    if response.status_code == 200:
        print("Пользователь успешно деактивирован")
        print(response)
    else:
        print(f"Ошибка при деактивации пользователя: {response.status_code} {response.text}")

    return response.text

def enable_user(userid):
     enable_url = f'http://{nextcloud_admin_user}:{nextcloud_admin_password}@{url}/ocs/v1.php/cloud/users/{userid}/enable'
     auth = HTTPBasicAuth(os.getenv("NEXTCLOUD_ADMIN_USER"), os.getenv("NEXTCLOUD_ADMIN_PASSWORD"))
     headers = {
         "OCS-APIRequest": "true"
     }
     data = {
         "userid": userid,
     }
     response = requests.put(enable_url, auth=auth, headers=headers, data=data)
     if response.status_code == 200:
         print("Пользователь успешно активирован")
         print(response)
     else:
         print(f"Ошибка при активации пользователя: {response.status_code} {response.text}")
     return response.text

def upload_text_file_to_nextcloud(file_content="1+1=2", file_name="calc.txt"):
    # Полный путь к файлу в Nextcloud
    full_url = f"http://{url}/remote.php/dav/files/{nextcloud_admin_user}/{file_name}"


    headers = {
        "Content-Type": "text/plain"
    }


    response = requests.put(full_url, data=file_content, headers=headers,
                            auth=HTTPBasicAuth(nextcloud_admin_user, nextcloud_admin_password))


    if response.status_code in [200, 201]:
        print("Файл успешно загружен.")
    else:
        print(f"Ошибка при загрузке файла: {response.status_code} {response.text}")

def upload_file():
    pass

# def upload_file_to_nextcloud(file_path):
#     request_url = f"http://{url}/remote.php/dav/files/USERNAME/"
#     headers = {'Content-Type': 'image/jpeg'}
#     auth = (nextcloud_admin_user, nextcloud_admin_password)
#     with open(file_path, 'rb') as file_data:
#         response = requests.put(request_url + 'path/to/save/image.jpg', data=file_data, headers=headers, auth=auth)
#         if response.status_code == 201:
#             return response.headers.get('Location')  # URL загруженного файла в Nextcloud
#         else:
#             return None