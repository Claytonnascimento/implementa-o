# Bucket Sort -
# Estavel? Sim
# Memória extra? Alta
# Vantagens: Excelente desempenho com dados uniformemente distribuídos. Pode ser mais rápido que o Quick Sort.
# Desvantagens: Requer função de distribuição adequada. Complexidade pode variar muito.
# O algoritmo bucket sort (ordenação por balde). 
# Este algoritmo é particularmente eficiente para ordenar dados com distribuição uniforme,
# especialmente números de ponto flutuante. 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(array):
    if len(array) == 0:
        return array

    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    max_val, min_val = max(array), min(array)
    if max_val == min_val:
        return array

    for num in array: 
        index = int((num - min_val) / (max_val - min_val) * (num_buckets - 1))
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i] = insertion_sort(buckets[i])

    arr_ordenado = []
    for bucket in buckets:
        arr_ordenado.extend(bucket)

    return arr_ordenado

print("Bucket Sort:", bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))
