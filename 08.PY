import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo_DAAC(destino_DAAC, asunto_DAAC, mensaje_DAAC):
    remitente_DAAC = "tu_email@gmail.com"
    clave_DAAC = "tu_contraseña_app"

    mensaje_obj_DAAC = MIMEMultipart()
    mensaje_obj_DAAC['From'] = remitente_DAAC
    mensaje_obj_DAAC['To'] = destino_DAAC
    mensaje_obj_DAAC['Subject'] = asunto_DAAC

    mensaje_obj_DAAC.attach(MIMEText(mensaje_DAAC, 'plain'))

    try:
        servidor_DAAC = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_DAAC.starttls()
        servidor_DAAC.login(remitente_DAAC, clave_DAAC)

        contenido_DAAC = mensaje_obj_DAAC.as_string()
        servidor_DAAC.sendmail(remitente_DAAC, destino_DAAC, contenido_DAAC)
        print("Correo enviado exitosamente DAAC")
    except Exception as error_DAAC:
        print(f"Error al enviar correo DAAC: {error_DAAC}")
    finally:
        servidor_DAAC.quit()

enviar_correo_DAAC(
    "destino@example.com",
    "Prueba de correo DAAC",
    "Este es un correo enviado desde Python versión DAAC"
)
