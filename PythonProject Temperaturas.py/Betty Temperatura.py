import random

# Definir dimensiones de la matriz
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Crear una matriz 3D con temperaturas aleatorias (10°C a 35°C)
matriz_temperaturas = [[[random.randint(10, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas promedio para {ciudad}:")
    for semana in range(semanas):
        promedio = sum(matriz_temperaturas[i][semana]) / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()
