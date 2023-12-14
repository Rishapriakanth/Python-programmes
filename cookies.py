#You have a collection of candies, and each candy has a certain sweetness value. Your goal is to combine the candies to create new candies until you reach a specific target sweetness level. Find how many steps need to reach candies sweetness target.
#sweetness = (least sweet candy + 2 * second least sweet candy)
import sys
import heapq

def minStepsToReachTargetSweetness(target, candies):
    heapq.heapify(candies)

    steps = 0
    while candies[0] < target:
        if len(candies) < 2:
            return -1

        first = heapq.heappop(candies)
        second = heapq.heappop(candies)
        new_sweetness = first + 2 * second
        heapq.heappush(candies, new_sweetness)
        steps += 1

    return steps

target1 = int(input())
candies1 = list(map(int,input().split()))
output1 = minStepsToReachTargetSweetness(target1, candies1)
print(output1)
