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
