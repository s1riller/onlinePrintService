import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Информация для входа
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_address ="miheev.saveliy.2002@gmail.com"
email_password = "GMaga2020"

# Информация о сообщении
recipient_email = 'gg@ggjp.ru'
subject = 'Тема письма'
body = 'Текст письма'

# Создание объекта сообщения
message = MIMEMultipart()
message['From'] = email_address
message['To'] = recipient_email
message['Subject'] = subject

# Добавление текста в тело сообщения
message.attach(MIMEText(body, 'plain'))

# Установка соединения с SMTP сервером и отправка сообщения
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Активация безопасного соединения
    server.login(email_address, email_password)  # Вход
    text = message.as_string()
    server.sendmail(email_address, recipient_email, text)
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    server.quit()
