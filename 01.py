def calcular_promedio_DAAC(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def determinar_estado_DAAC(promedio):
    if promedio >= 6.0:
        return "APROBADO"
    else:
        return "REPROBADO"

print("=== SISTEMA DE NOTAS DAAC ===")

nota1_DAAC = float(input("Nota 1: "))
nota2_DAAC = float(input("Nota 2: "))
nota3_DAAC = float(input("Nota 3: "))

promedio_DAAC = calcular_promedio_DAAC(nota1_DAAC, nota2_DAAC, nota3_DAAC)
estado_DAAC = determinar_estado_DAAC(promedio_DAAC)

print(f"\nPromedio: {promedio_DAAC:.2f}")
print(f"Estado: {estado_DAAC}")
