# Insertion Sort (ordenação por inserção) -
# Estavel? Sim
# Memória extra? Baixa
# Vantagens: Excelente para listas pequenas. Muito eficiente para listas quase ordenadas.
# Desvantagens: Desempenho ruim em listas grandes (O(n²)).
# A função insertion_sort(arr) percorre a lista arr, e para cada elemento, compara-o com os elementos anteriores 
# e o insere na posição correta para manter a parte inicial da lista sempre ordenada. 

valores = [29, 10, 14, 37, 14, 3, 76, 45, 20]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
    
print("Insertion Sort:", insertion_sort(valores.copy()))
