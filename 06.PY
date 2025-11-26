import pandas as pd

datos_DAAC = {
    'Nombre_DAAC': ['Ana', 'Luis', 'María', 'Carlos'],
    'Edad_DAAC': [25, 30, 22, 35],
    'Ciudad_DAAC': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Salario_DAAC': [30000, 45000, 28000, 52000]
}

df_DAAC = pd.DataFrame(datos_DAAC)
print(df_DAAC)

print("\n--- ESTADÍSTICAS DAAC ---")
print(df_DAAC.describe())

mayores_30_DAAC = df_DAAC[df_DAAC['Edad_DAAC'] > 30]
print("\n--- MAYORES DE 30 DAAC ---")
print(mayores_30_DAAC)

df_ordenado_DAAC = df_DAAC.sort_values('Salario_DAAC', ascending=False)
print("\n--- ORDENADO POR SALARIO DAAC ---")
print(df_ordenado_DAAC)

promedio_edad_DAAC = df_DAAC['Edad_DAAC'].mean()
promedio_salario_DAAC = df_DAAC['Salario_DAAC'].mean()

print(f"\nPromedio edad DAAC: {promedio_edad_DAAC}")
print(f"Promedio salario DAAC: ${promedio_salario_DAAC}")
