# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero de Software"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor (ya existe "profesion", así que este paso está cumplido)
informacion_personal["correo"] = "carlos.perez@example.com"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final


