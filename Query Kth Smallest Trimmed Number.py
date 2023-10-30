#given input is 113 933 231 719,
#Take first query 1 1 (here first 1 is position , second is selecting a digit from right)
# So each digit we need to take one digit value form right - 113 is 3, 933 is 3 231 is 1 719 is 9 [ 3 3 1 9 ] so the first smallest value is 1 ,
#then the index value of 1 is 2.
#Second query 2 2 So each digit we need to take two digit value form right.So we get [ 13 33 31 19 ] first smallest value 19 ,
#then the index value of 19 is 3.

def kth_smallest_trimmed_number(nums, queries):
    answers = []
    for query in queries:
        position, trim_length = query[0], query[1]
        trimmed_nums = [num[-trim_length:] for num in nums]
        sorted_nums = sorted(enumerate(trimmed_nums), key=lambda x: x[1])
        index = sorted_nums[position - 1][0]
        answers.append(index)
    return answers

nums = input().split()
num_queries = int(input())

queries = []
for _ in range(num_queries):
    query_str = input()
    position, trim_length = map(int, query_str.split())
    queries.append([position, trim_length])

output = kth_smallest_trimmed_number(nums, queries)
for i in output:
    print(i,end=' ')