# Merge Sort (ordenação por intercalação) -
# Estavel? sim
# Memória extra? Alta
# Vantagens: Muito eficiente (O(n log n)). Estável (mantém a ordem relativa).
# Desvantagens: Requer memória extra. Mais difícil de implementar manualmente.
# A função mega sort funciona dividindo recursivamente a lista até que cada sublista tenha um único elemento e, 
# em seguida, mesclando e ordenando essas sublistas para formar a lista final ordenada.  


valores = [29, 10, 14, 37, 14, 3, 76, 45, 20]

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
    return arr

print("Merge Sort:", merge_sort(valores.copy()))
