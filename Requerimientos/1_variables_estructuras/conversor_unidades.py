# Conversor de unidades: Celsius a Fahrenheit y metros a kilómetros
def celsius_a_fahrenheit(c):
    return c * 9/5 + 32
def metros_a_kilometros(m):
    return m / 1000
# Entrada de datos
temp = float(input("Ingrese temperatura en Celsius: "))
longitud = float(input("Ingrese longitud en metros: "))
# Conversión
print(f"{temp}°C = {celsius_a_fahrenheit(temp)}°F")
print(f"{longitud} m = {metros_a_kilometros(longitud)} km")
