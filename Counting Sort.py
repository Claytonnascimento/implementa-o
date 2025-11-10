# Counting Sort (Ordenação por Contagem).
# Este algoritmo é eficiente para ordenar listas de números inteiros positivos
# quando a diferença entre o maior e o menor valor não é muito grande [1].

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    arr_ordenado = []
    for i in range(len(count)):
        arr_ordenado.extend([i] * count[i])
    return arr_ordenado
    
print("Counting Sort:", counting_sort([4, 2, 2, 8, 3, 3, 1]))
