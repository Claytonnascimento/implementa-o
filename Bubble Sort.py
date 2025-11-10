valores = [29, 10, 14, 37, 14, 3, 76, 45, 20]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort(valores.copy()))
