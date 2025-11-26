print("=== CALCULADORA INTERACTIVA DAAC ===")

nombreDAAC = input("¿Cuál es tu nombre? ")
print(f"Hola {nombreDAAC}, vamos a calcular.")

numero1DAAC = float(input("Primer número: "))
numero2DAAC = float(input("Segundo número: "))

print("Operaciones disponibles: +, -, *, /")
operacionDAAC = input("¿Qué operación deseas? ")

if operacionDAAC == "+":
    resultadoDAAC = numero1DAAC + numero2DAAC
    simboloDAAC = "+"
elif operacionDAAC == "-":
    resultadoDAAC = numero1DAAC - numero2DAAC
    simboloDAAC = "-"
elif operacionDAAC == "*":
    resultadoDAAC = numero1DAAC * numero2DAAC
    simboloDAAC = "x"
elif operacionDAAC == "/":
    if numero2DAAC != 0:
        resultadoDAAC = numero1DAAC / numero2DAAC
    else:
        resultadoDAAC = "Error: division por cero"
    simboloDAAC = "/"
else:
    resultadoDAAC = "Operacion no valida"
    simboloDAAC = "?"

print("RESULTADO DAAC:")
print(f"{numero1DAAC} {simboloDAAC} {numero2DAAC} = {resultadoDAAC}")
