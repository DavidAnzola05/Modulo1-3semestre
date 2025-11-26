from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def enviar_correo_html_DAAC(destinatario_DAAC, asunto_DAAC):
    html_DAAC = """
    <html>
    <body style="font-family: Arial; background-color:#f6f6f6; padding:20px;">
        <div style="max-width:600px; margin:auto; background:white; padding:20px; border-radius:8px;">
            <h2 style="color:#4CAF50;">¡Bienvenido a nuestro servicio!</h2>

            <p>Hola <strong>{nombre}</strong>,</p>

            <p>
                Gracias por registrarte. Tu cuenta ha sido creada exitosamente.
            </p>

            <p>
                <strong>Usuario:</strong> {usuario}<br>
                <strong>Fecha de registro:</strong> {fecha}
            </p>

            <a href="#" style="
                background:#4CAF50;
                color:white;
                padding:10px 20px;
                text-decoration:none;
                border-radius:5px;
            ">Comienza a usar tu cuenta ahora</a>

            <p style="margin-top:30px; font-size:12px; color:#555;">
                Si no solicitaste esta cuenta, simplemente ignora este mensaje.
            </p>
        </div>
    </body>
    </html>
    """

    html_personalizado_DAAC = html_DAAC.format(
        nombre="María García",
        usuario="maria_garcia",
        fecha="15/01/2024"
    )

    msg_DAAC = MIMEMultipart('alternative')
    msg_DAAC['Subject'] = asunto_DAAC
    msg_DAAC['From'] = "tu_email@gmail.com"
    msg_DAAC['To'] = destinatario_DAAC

    parte_html_DAAC = MIMEText(html_personalizado_DAAC, 'html')
    msg_DAAC.attach(parte_html_DAAC)

    try:
        servidor_DAAC = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_DAAC.starttls()
        servidor_DAAC.login("tu_email@gmail.com", "TU_CONTRASEÑA_DE_APP")
        servidor_DAAC.sendmail(msg_DAAC['From'], msg_DAAC['To'], msg_DAAC.as_string())
        servidor_DAAC.quit()
        print("Correo enviado correctamente DAAC.")
    except Exception as e:
        print("Error al enviar el correo DAAC:", e)
