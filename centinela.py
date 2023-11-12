import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psutil
import time
import os

# Obtener información sobre la memoria RAM
def get_ram_info():
    mem = psutil.virtual_memory()
    total_ram_gb = bytes_to_gb(mem.total)
    available_ram_gb = bytes_to_gb(mem.available)
    used_ram_gb = bytes_to_gb(mem.used)
    return total_ram_gb, available_ram_gb, used_ram_gb, mem.percent

# Convertir bytes a gigabytes
def bytes_to_gb(bytes):
    return bytes / (1024 ** 3)

# Enviar correo electrónico con los datos de la RAM
def send_ram_email():
    total_ram_gb, available_ram_gb, used_ram_gb, porcentaje_ram = get_ram_info()
    
    # Enviar correo solo si la RAM utilizada supera los 3 GB
    if used_ram_gb > 2.5:
        # Datos para la cuenta de correo
        correo_emisor = ""  # Correo
        contraseña = ""  # Llave del correo

        # Datos para el correo electrónico
        correo_destinatario = ""  # Destinatario
        asunto = ""  # Asunto del correo
        cuerpo = f"""
        Memoria RAM Total: {total_ram_gb:.2f} GB
        Memoria RAM Disponible: {available_ram_gb:.2f} GB
        Memoria RAM Utilizada: {used_ram_gb:.2f} GB
        Porcentaje de RAM Utilizada: {porcentaje_ram}%
        Te recordamos que este correo fue generado de forma automática, favor de no responder.
        """

        # Configuración del servidor SMTP de Gmail
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Crear un mensaje de correo electrónico
        mensaje = MIMEMultipart()
        mensaje["From"] = correo_emisor
        mensaje["To"] = correo_destinatario
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(cuerpo, "plain"))

        # Iniciar una conexión SMTP segura
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Iniciar sesión y enviar el correo electrónico
            server.login(correo_emisor, contraseña)
            server.sendmail(correo_emisor, correo_destinatario, mensaje.as_string())

        print("Correo electrónico enviado con éxito.")

# Bucle para enviar correos cada X segundos (por ejemplo, cada 3600 segundos = 1 hora)
while True:
    send_ram_email()
    print("CENTINELA")
    time.sleep(3600)  # Esperar 1 hora antes de enviar el siguiente correo
    os.system('cls')
