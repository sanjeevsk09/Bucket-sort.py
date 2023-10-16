def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr, num_buckets):
    if len(arr) == 0:
        return arr

    # Determine the range of input values
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / num_buckets

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Place elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)

    # Sort each bucket (you can use another sorting algorithm here)
    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Concatenate sorted buckets to get the final result
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

# Example usage:
arr = [3.2, 1.8, 4.5, 2.7, 2.1, 1.1]
num_buckets = 5
sorted_arr = bucket_sort(arr, num_buckets)
print(sorted_arr)
