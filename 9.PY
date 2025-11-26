from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def enviar_correo_html(destinatario, asunto):
    """Envía un correo con contenido HTML"""

    # --- Contenido HTML con diseño básico ---
    html = """
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

    # Personalizar el HTML
    html_personalizado = html.format(
        nombre="María García",
        usuario="maria_garcia",
        fecha="15/01/2024"
    )

    # --- Construcción del correo ---
    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = "tu_email@gmail.com"
    msg['To'] = destinatario

    # Parte HTML
    parte_html = MIMEText(html_personalizado, 'html')
    msg.attach(parte_html)

    # --- Enviar correo ---
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login("tu_email@gmail.com", "TU_CONTRASEÑA_DE_APP")
        servidor.sendmail(msg['From'], msg['To'], msg.as_string())
        servidor.quit()

        print("Correo enviado correctamente.")

    except Exception as e:
        print("Error al enviar el correo:", e)
