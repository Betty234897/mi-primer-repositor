def ordenar_fila(matriz, fila):
    matriz[fila].sort()  # Ordenamos la fila en orden ascendente

# Definir la matriz 3x3
matriz_ordenacion = [
    [12, 5, 8],
    [3, 9, 1],
    [4, 7, 6]
]

fila_a_ordenar = int(input("Ingrese el índice de la fila a ordenar (0-2): "))
print("Matriz original:")
for fila in matriz_ordenacion:
    print(fila)

ordenar_fila(matriz_ordenacion, fila_a_ordenar)

print("Matriz con la fila ordenada:")
for fila in matriz_ordenacion:
    print(fila)
1
