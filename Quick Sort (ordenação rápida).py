# A função quick_sort é recursiva, ou seja, ela chama a si mesma para resolver partes menores do problema (ordenar sub-listas),
# até que toda a lista esteja ordenada. 

valores = [29, 10, 14, 37, 14, 3, 76, 45, 20]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivo]
        iguais = [x for x in arr if x == pivo]
        maiores = [x for x in arr if x > pivo]
        return quick_sort(menores) + iguais + quick_sort(maiores)

print("Quick Sort:", quick_sort(valores.copy()))
