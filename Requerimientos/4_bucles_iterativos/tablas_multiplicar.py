# Generador tabla de multiplicar
numero = int(input("Ingrese un número para ver su tabla: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Calculadora de factorial
n = int(input("Ingrese un número: "))
resultado = 1
i = 1

while i <= n:
    resultado *= i
    i += 1

print(f"El factorial de {n} es {resultado}")
