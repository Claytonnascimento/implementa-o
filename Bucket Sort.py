def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    max_val, min_val = max(arr), min(arr)
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * num_buckets)
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i] = insertion_sort(buckets[i])

    arr_ordenado = []
    for bucket in buckets:
        arr_ordenado.extend(bucket)
    return arr_ordenado

print("Bucket Sort:", bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))
