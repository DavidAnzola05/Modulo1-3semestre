from sklearn.linear_model import LinearRegression
import numpy as np

tamanos_DAAC = np.array([[50], [60], [70], [80], [90], [100], [110], [120]])
precios_DAAC = np.array([150, 170, 190, 210, 230, 250, 270, 290])

modelo_DAAC = LinearRegression()
modelo_DAAC.fit(tamanos_DAAC, precios_DAAC)

print("Modelo entrenado exitosamente")
print(f"Coeficiente: {modelo_DAAC.coef_[0]:.2f}")
print(f"Intercepto: {modelo_DAAC.intercept_:.2f}")

nueva_casa_DAAC = np.array([[85]])
precio_predicho_DAAC = modelo_DAAC.predict(nueva_casa_DAAC)
print(f"\nUna casa de 85 m2 costaría aproximadamente ${precio_predicho_DAAC[0]:.2f}k")

casas_nuevas_DAAC = np.array([[65], [95], [105]])
predicciones_DAAC = modelo_DAAC.predict(casas_nuevas_DAAC)

print("\nPredicciones para varias casas:")
for tamano_DAAC, precio_DAAC in zip(casas_nuevas_DAAC, predicciones_DAAC):
    print(f" {tamano_DAAC[0]} m2 → ${precio_DAAC:.2f}k")
