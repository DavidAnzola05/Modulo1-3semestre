print("SISTEMA DE CALIFICACIONES DAAC")

calificacionDAAC = float(input("Ingresa tu calificación (0-100): "))

if calificacionDAAC < 0 or calificacionDAAC > 100:
    print("Error: rango inválido")
else:
    if calificacionDAAC >= 90:
        letraDAAC = "A"
        mensajeDAAC = "Excelente"
    elif calificacionDAAC >= 80:
        letraDAAC = "B"
        mensajeDAAC = "Muy bien"
    elif calificacionDAAC >= 70:
        letraDAAC = "C"
        mensajeDAAC = "Bien"
    elif calificacionDAAC >= 60:
        letraDAAC = "D"
        mensajeDAAC = "Suficiente"
    else:
        letraDAAC = "F"
        mensajeDAAC = "Reprobado"

    print(letraDAAC)
    print(mensajeDAAC)

    if calificacionDAAC >= 90:
        print("Sigue así")
    elif calificacionDAAC >= 70:
        print("Puedes mejorar")
    else:
        print("Necesitas estudiar más")
print("FIN DEL SISTEMA DE CALIFICACIONES DAAC")