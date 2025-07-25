# Formulario de usuario: captura de datos básicos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura en metros: "))
suscrito = input("¿Está suscrito al boletín? (sí/no): ").lower() == "sí"

print("\nDatos registrados:")
print(f"Nombre: {nombre} (tipo: {type(nombre)})")
print(f"Edad: {edad} (tipo: {type(edad)})")
print(f"Estatura: {estatura} m (tipo: {type(estatura)})")
print(f"Suscripción activa: {suscrito} (tipo: {type(suscrito)})")
