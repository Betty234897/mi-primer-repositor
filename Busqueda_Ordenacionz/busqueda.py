def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Definir la matriz 3x3
matriz = [
    [5, 8, 2],
    [4, 1, 9],
    [7, 6, 3]
]

valor_buscado = int(input("Ingrese el valor a buscar: "))
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"El valor {valor_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
7
