# operadores.py

# Solicitar los dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Operaciones básicas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Validar división entre cero
if num2 != 0:
    division = num1 / num2
    division_entera = num1 // num2
    residuo = num1 % num2
else:
    division = "No se puede dividir entre cero"
    division_entera = "No se puede dividir entre cero"
    residuo = "No se puede dividir entre cero"

potencia = num1 ** num2

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Residuo: {residuo}")
print(f"Potencia: {potencia}")