from telegram import Bot
import asyncio

class TelegramNotificadorDAAC:
    def __init__(self, token_DAAC, chat_id_DAAC):
        self.token_DAAC = token_DAAC
        self.chat_id_DAAC = chat_id_DAAC
        self.bot_DAAC = Bot(token=self.token_DAAC)

    async def enviar_mensaje_DAAC(self, texto_DAAC):
        try:
            await self.bot_DAAC.send_message(
                chat_id=self.chat_id_DAAC,
                text=texto_DAAC
            )
            print("Mensaje enviado Telegram DAAC")
        except Exception as e_DAAC:
            print("Error DAAC:", e_DAAC)

    async def enviar_archivo_DAAC(self, ruta_archivo_DAAC):
        try:
            with open(ruta_archivo_DAAC, 'rb') as archivo_DAAC:
                await self.bot_DAAC.send_document(
                    chat_id=self.chat_id_DAAC,
                    document=archivo_DAAC
                )
            print("Archivo enviado Telegram DAAC")
        except Exception as e_DAAC:
            print("Error DAAC:", e_DAAC)

async def main_DAAC():
    notificador_DAAC = TelegramNotificadorDAAC(
        token_DAAC="TU_TOKEN_AQUI",
        chat_id_DAAC="TU_CHAT_ID"
    )
    await notificador_DAAC.enviar_mensaje_DAAC("Proceso completado DAAC")
    await notificador_DAAC.enviar_archivo_DAAC("reporte.pdf")

asyncio.run(main_DAAC())
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib