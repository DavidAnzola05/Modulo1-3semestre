from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def crear_pdf_tabla_DAAC():
    doc_DAAC = SimpleDocTemplate("ventas_detalladas_DAAC.pdf", pagesize=letter)
    elementos_DAAC = []
    estilos_DAAC = getSampleStyleSheet()
    titulo_estilo_DAAC = estilos_DAAC['Title']

    titulo_DAAC = Paragraph("Ventas por Producto DAAC", titulo_estilo_DAAC)
    elementos_DAAC.append(titulo_DAAC)

    datos_DAAC = [
        ['Producto DAAC', 'Cantidad DAAC', 'Precio DAAC', 'Total DAAC'],
        ['Laptop Pro DAAC', '15', '$1,200', '$18,000'],
        ['Mouse Inalámbrico DAAC', '45', '$25', '$1,125'],
        ['Teclado Mecánico DAAC', '30', '$60', '$1,800'],
        ['Monitor 24 DAAC', '20', '$300', '$6,000'],
        ['', '', 'TOTAL DAAC:', '$26,925']
    ]

    tabla_DAAC = Table(datos_DAAC)
    tabla_DAAC.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('BACKGROUND', (0,1), (-1,-2), colors.beige),
        ('GRID', (0,0), (-1,-2), 1, colors.black),
        ('BACKGROUND', (0,-1), (-1,-1), colors.lightblue),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,-1), (-1,-1), 12),
    ]))

    elementos_DAAC.append(tabla_DAAC)
    doc_DAAC.build(elementos_DAAC)
    print("PDF con tabla creado DAAC")

crear_pdf_tabla_DAAC()
