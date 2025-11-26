from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X_DAAC = np.array([
    [25, 30, 2],
    [30, 45, 5],
    [35, 60, 8],
    [40, 80, 12],
    [22, 25, 1],
    [28, 40, 4],
    [45, 90, 15],
    [50, 100, 20]
])

y_DAAC = np.array([0, 0, 1, 1, 0, 0, 1, 1])

X_train_DAAC, X_test_DAAC, y_train_DAAC, y_test_DAAC = train_test_split(
    X_DAAC, y_DAAC, test_size=0.25, random_state=42
)

modelo_DAAC = DecisionTreeClassifier()
modelo_DAAC.fit(X_train_DAAC, y_train_DAAC)

precision_DAAC = modelo_DAAC.score(X_test_DAAC, y_test_DAAC)
print(f"Precisión del modelo: {precision_DAAC*100:.1f}%")

nuevos_clientes_DAAC = np.array([
    [32, 55, 7],
    [24, 28, 2]
])

predicciones_DAAC = modelo_DAAC.predict(nuevos_clientes_DAAC)

print("\nPredicciones:")
for i_DAAC, pred_DAAC in enumerate(predicciones_DAAC):
    resultado_DAAC = "SÍ comprará" if pred_DAAC == 1 else "NO comprará"
    print(f"Cliente {i_DAAC+1}: {resultado_DAAC} el producto premium")
from sklearn.tree import DecisionTreeClassifier