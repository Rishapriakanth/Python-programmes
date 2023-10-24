def sliding_subarray(arr, k, n):
    result = []
    for i in range(len(arr) - k + 2):
        subarray = arr[i:i + k]
        sorted_subarray = sorted(subarray)
        result.append(sorted_subarray[n - 1])
    return result


arr = list(map(int, input().split()))
k = int(input())
n = int(input())

out = sliding_subarray(arr, k, n)
print(' '.join(map(str, out)))

