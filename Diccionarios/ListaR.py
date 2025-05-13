usuarios = {
    "Luisa":"GERENTE",
    "Martin":"SISTEMAS",
    "Andres":"RR.HH"
}

nombre = input("Nombre de usuario: ")

if nombre in usuarios:
    print("Rol:", usuarios[nombre])
else:
    print("Usuario no existe.")