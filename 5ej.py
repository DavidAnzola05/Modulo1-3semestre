print("BUCLES PYTHON DAAC")
print("=" * 30)

print("1. Contando 1 al 5:")
for numeroDAAC in range(1, 6):
    print(numeroDAAC)

print("-" * 30)

print("2. Lista de frutas:")
frutasDAAC = ["manzana", "banana", "naranja", "uva"]
for frutaDAAC in frutasDAAC:
    print(frutaDAAC)

print("-" * 30)

print("3. Contador con while:")
contadorDAAC = 1
while contadorDAAC <= 3:
    print(contadorDAAC)
    contadorDAAC += 1

print("-" * 30)

print("4. Buscar número:")
numerosDAAC = [10, 25, 30, 45, 50]
buscarDAAC = 30

for xDAAC in numerosDAAC:
    print(xDAAC)
    if xDAAC == buscarDAAC:
        print("Encontrado")
        break

print("-" * 30)

print("5. Solo pares:")
for iDAAC in range(1, 11):
    if iDAAC % 2 != 0:
        continue
    print(iDAAC)

print("-" * 30)

print("6. Menú interactivo:")
while True:
    print("1. Saludar")
    print("2. Cuadrado")
    print("3. Salir")
    opcionDAAC = input("Elige: ")

    if opcionDAAC == "1":
        nombreDAAC = input("Nombre: ")
        print("Hola", nombreDAAC)
    elif opcionDAAC == "2":
        numeroDAAC = int(input("Número: "))
        cuadradoDAAC = numeroDAAC ** 2
        print(cuadradoDAAC)
    elif opcionDAAC == "3":
        print("Adiós")
        break
    else:
        print("Inválido")
