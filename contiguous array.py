#contiguous arrays in python
#Given a binary array 'nums',
#you are required to find the maximum length of a contiguous subarray that contains an equal number of 0s and 1s.
def findMaxLength(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1
    sum_index_map = {0: -1}
    max_length = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum])
        else:
            sum_index_map[current_sum] = i

    return max_length

n=list(map(int,input().split()))
x=findMaxLength(n)
print(x)
