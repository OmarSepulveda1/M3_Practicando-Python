# Agenda de contactos
agenda = {}

while True:
    nombre = input("Nombre (dejar vacío para salir): ")
    if nombre == "":
        break
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print("\n📇 Contactos registrados:")
for nombre, telefono in agenda.items():
    print(f"{nombre}: {telefono}")
