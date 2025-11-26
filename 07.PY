import matplotlib.pyplot as plt

meses_DAAC = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas_DAAC = [12000, 15000, 13000, 18000, 21000]

plt.figure(figsize=(10, 6))
plt.plot(meses_DAAC, ventas_DAAC, marker='o', linewidth=2)
plt.title('Ventas Mensuales 2024 DAAC')
plt.xlabel('Mes DAAC')
plt.ylabel('Ventas ($) DAAC')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(meses_DAAC, ventas_DAAC)
plt.title('Ventas por Mes DAAC')
plt.xlabel('Mes DAAC')
plt.ylabel('Ventas ($) DAAC')
plt.show()

categorias_DAAC = ['Electrónica', 'Ropa', 'Alimentos']
valores_DAAC = [35, 25, 40]

plt.figure(figsize=(8, 8))
plt.pie(valores_DAAC, labels=categorias_DAAC, autopct='%1.1f%%')
plt.title('Ventas por Categoría DAAC')
plt.show()
