import smtplib
from email.mime.text import MIMEText

# Информация об отправителе и получателе
sender = 'beerbee@gmail.com'
receiver = 'deniss.hohlov@gmail.com'

# Текст электронного письма
message = '''Hello,

This is a test email sent from Python.

Best regards,
Your Name'''

# Создание экземпляра MIMEText
msg = MIMEText(message)

# Заголовки электронного письма
msg['Subject'] = 'Test Email from Python'
msg['From'] = sender
msg['To'] = receiver

# Подключение к серверу SMTP
server = smtplib.SMTP('smtp.example.com')

# Отправка электронного письма
server.sendmail(sender, receiver, msg.as_string())

# Закрытие соединения с сервером
server.quit()
