from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def crear_pdf_simple_DAAC():
    c_DAAC = canvas.Canvas("reporte_DAAC.pdf", pagesize=letter)
    ancho_DAAC, alto_DAAC = letter

    c_DAAC.setFont("Helvetica-Bold", 24)
    c_DAAC.drawString(100, alto_DAAC - 100, "Reporte Mensual de Ventas DAAC")

    c_DAAC.setFont("Helvetica", 14)
    c_DAAC.drawString(100, alto_DAAC - 130, "Enero 2024 DAAC")

    c_DAAC.line(100, alto_DAAC - 140, ancho_DAAC - 100, alto_DAAC - 140)

    c_DAAC.setFont("Helvetica", 12)
    y_DAAC = alto_DAAC - 180

    textos_DAAC = [
        "Total de ventas DAAC: $45,000",
        "Número de transacciones DAAC: 127",
        "Producto más vendido DAAC: Laptop Pro",
        "Crecimiento vs mes anterior DAAC: +15%"
    ]

    for t_DAAC in textos_DAAC:
        c_DAAC.drawString(100, y_DAAC, t_DAAC)
        y_DAAC -= 25

    c_DAAC.save()
    print("PDF creado DAAC: reporte_DAAC.pdf")

crear_pdf_simple_DAAC()
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas