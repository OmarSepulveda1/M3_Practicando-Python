# Calculadora de áreas

def area_circulo(radio):
    return 3.1416 * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

print("1. Círculo\n2. Rectángulo")
op = input("Elija figura: ")

if op == "1":
    r = float(input("Radio: "))
    print(f"Área del círculo: {area_circulo(r)}")
elif op == "2":
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print(f"Área del rectángulo: {area_rectangulo(b, h)}")
else:
    print("Opción no válida.")
