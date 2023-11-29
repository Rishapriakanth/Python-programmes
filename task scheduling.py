#There are N tasks of varying durations, represented by an array A of size N.
# K workers are available, and each worker takes 1 unit of time to complete 1 unit of work.
# The goal is to find the minimum time required to complete all the tasks, with the constraint that each worker can only work on a continuous sequence of tasks.
import sys
def is_valid(mid, tasks, workers):
    current_worker = 0
    current_time = 0

    for task_time in tasks:
        if current_time + task_time > mid:
            current_worker += 1
            current_time = 0

        current_time += task_time

    return current_worker + 1 <= workers


def min_time_to_complete(tasks, workers):
    low, high = max(tasks), sum(tasks)

    while low < high:
        mid = (low + high) // 2
        if is_valid(mid, tasks, workers):
            high = mid
        else:
            low = mid + 1

    return low


n = int(input())
tasks_input = list(map(int, input().split()))
workers_input = int(input())
result = min_time_to_complete(tasks_input, workers_input)
print(result)

