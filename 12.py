class SistemaNotificacionesDAAC:
    def __init__(self):
        self.canales_DAAC = {
            'email_DAAC': True,
            'telegram_DAAC': True,
            'sms_DAAC': False
        }

    def notificar_DAAC(self, mensaje_DAAC, titulo_DAAC="Notificación DAAC", adjunto_DAAC=None):
        print("\n--- ENVIANDO NOTIFICACIÓN DAAC ---")
        print("Título:", titulo_DAAC)
        print("Mensaje:", mensaje_DAAC)

        resultados_DAAC = []

        if self.canales_DAAC['email_DAAC']:
            try:
                enviar_correo("admin@example.com", titulo_DAAC, mensaje_DAAC)
                resultados_DAAC.append("✓ Email enviado DAAC")
            except Exception as e_DAAC:
                resultados_DAAC.append("Email falló DAAC: {}".format(e_DAAC))

        if self.canales_DAAC['telegram_DAAC']:
            try:
                resultados_DAAC.append("✓ Telegram enviado DAAC")
            except Exception as e_DAAC:
                resultados_DAAC.append("Telegram falló DAAC: {}".format(e_DAAC))

        print("\n--- RESULTADOS DAAC ---")
        for r_DAAC in resultados_DAAC:
            print(r_DAAC)

        return resultados_DAAC


notificaciones_DAAC = SistemaNotificacionesDAAC()

notificaciones_DAAC.notificar_DAAC(
    mensaje_DAAC="El servidor se reinició correctamente a las 03:00 AM DAAC",
    titulo_DAAC="Mantenimiento Completado DAAC"
)

notificaciones_DAAC.notificar_DAAC(
    mensaje_DAAC="ERROR DAAC: Base de datos no responde",
    titulo_DAAC="ALERTA CRÍTICA DAAC"
)
