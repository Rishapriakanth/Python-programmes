#Given a 1-indexed array initially filled with zeros and a list of operations, perform each operation by adding a value to each element of the array between two given indices (inclusive). After performing all operations, find and return the maximum value in the array.
def mix_array(arr_size, queries):
    array = [0] * (arr_size + 1)

    for query in queries:
        start, end, value = query
        array[start - 1] += value
        array[end] -= value

    max_value = current_sum = 0
    for value in array:
        current_sum += value
        max_value = max(max_value, current_sum)

    return max_value

arr_size1 = int(input())
query_count1 = int(input())
queries1 = []
for _ in range(query_count1):
    query = list(map(int, input().split()))
    queries1.append(query)
output1 = mix_array(arr_size1, queries1)
print(output1)

