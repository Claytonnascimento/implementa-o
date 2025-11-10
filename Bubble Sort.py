# Bubble Sort -
# Estavel? sim
# Memória extra? Baixa
# Vantagens: Fácil de implementar. Bom para listas pequenas ou quase ordenadas.
# Desvantagens: Muito ineficiente para grandes volumes (O(n²)). Realiza muitas comparações desnecessárias.
# O algoritmo Bubble Sort é um método de ordenação que compara pares de elementos adjacentes.
# Os elementos são trocados se estiverem na ordem errada.
# Este processo é repetido até que a lista esteja completamente ordenada.

valores = [29, 10, 14, 37, 14, 3, 76, 45, 20]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort(valores.copy()))
