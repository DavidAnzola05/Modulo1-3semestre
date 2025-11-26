from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime

class GeneradorReportes_DAAC:
    def __init__(self, titulo_DAAC, autor_DAAC="Sistema Automatizado DAAC"):
        self.titulo_DAAC = titulo_DAAC
        self.autor_DAAC = autor_DAAC
        self.elementos_DAAC = []
        self.estilos_DAAC = getSampleStyleSheet()
        self.estilo_destacado_DAAC = ParagraphStyle(
            'Destacado_DAAC',
            parent=self.estilos_DAAC['Normal'],
            fontSize=14,
            textColor=colors.HexColor('#2E86AB'),
            spaceAfter=10,
            fontName='Helvetica-Bold'
        )

    def agregar_portada_DAAC(self):
        titulo_DAAC = Paragraph(self.titulo_DAAC, self.estilos_DAAC['Title'])
        self.elementos_DAAC.append(titulo_DAAC)
        self.elementos_DAAC.append(Spacer(1, 20))
        fecha_DAAC = datetime.now().strftime("%d de %B de %Y")
        subtitulo_DAAC = Paragraph(f"Generado el {fecha_DAAC}", self.estilos_DAAC['Normal'])
        self.elementos_DAAC.append(subtitulo_DAAC)
        self.elementos_DAAC.append(Spacer(1, 10))
        autor_DAAC = Paragraph(f"Por: {self.autor_DAAC}", self.estilos_DAAC['Normal'])
        self.elementos_DAAC.append(autor_DAAC)
        self.elementos_DAAC.append(PageBreak())

    def agregar_seccion_DAAC(self, titulo_DAAC, contenido_DAAC):
        titulo_seccion_DAAC = Paragraph(titulo_DAAC, self.estilo_destacado_DAAC)
        self.elementos_DAAC.append(titulo_seccion_DAAC)
        parrafo_DAAC = Paragraph(contenido_DAAC, self.estilos_DAAC['Normal'])
        self.elementos_DAAC.append(parrafo_DAAC)
        self.elementos_DAAC.append(Spacer(1, 15))

    def agregar_tabla_DAAC(self, datos_DAAC, titulo_DAAC=None):
        if titulo_DAAC:
            titulo_tabla_DAAC = Paragraph(titulo_DAAC, self.estilo_destacado_DAAC)
            self.elementos_DAAC.append(titulo_tabla_DAAC)

        tabla_DAAC = Table(datos_DAAC)
        tabla_DAAC.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ]))

        self.elementos_DAAC.append(tabla_DAAC)
        self.elementos_DAAC.append(Spacer(1, 20))

    def generar_DAAC(self, archivo_DAAC):
        doc_DAAC = SimpleDocTemplate(archivo_DAAC, pagesize=letter)
        doc_DAAC.build(self.elementos_DAAC)
        print(f"Reporte generado DAAC: {archivo_DAAC}")


reporte_DAAC = GeneradorReportes_DAAC("Reporte Trimestral de Ventas DAAC")
reporte_DAAC.agregar_portada_DAAC()
reporte_DAAC.agregar_seccion_DAAC(
    "Resumen Ejecutivo DAAC",
    "Este reporte presenta los resultados de ventas DAAC del primer trimestre del año..."
)

datos_ventas_DAAC = [
    ['Mes DAAC', 'Ventas DAAC', 'Crecimiento DAAC'],
    ['Enero', '$45,000', '10%'],
    ['Febrero', '$52,000', '15%'],
    ['Marzo', '$48,000', '-8%']
]

reporte_DAAC.agregar_tabla_DAAC(datos_ventas_DAAC, "Ventas Mensuales DAAC")
reporte_DAAC.generar_DAAC("reporte_trimestral_DAAC.pdf")
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle