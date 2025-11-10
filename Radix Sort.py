# Radix Sort -
# Estavel? Sim
# Memória extra? Alta
# Vantagens: Muito eficiente para números inteiros. Complexidade quase linear (O(nk)).
# Desvantagens: Requer memória adicional. Só funciona bem com inteiros.
# Esta função é uma variação do Counting Sort, adaptada para ordenar o array arr com base no dígito representado
# por exp (que pode ser 1 para unidades, 10 para dezenas, 100 para centenas, e assim por diante).

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
    return arr

print("Radix Sort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
