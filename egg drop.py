# you are provided X eggs.
# Your mission is to devise an ingenious strategy to determine the exact value of 'f' using the fewest possible egg drops, while ensuring that once you find 'f', you are absolutely certain about its value.
import sys
def egg_drop(eggs, floors):
    # Create a 2D table to store results of subproblems
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    # Base case: If there is only one egg, the minimum attempts are equal to the number of floors
    for i in range(1, floors + 1):
        dp[1][i] = i

    # Fill the rest of the table using optimal substructure property
    for egg in range(2, eggs + 1):
        for floor in range(1, floors + 1):
            dp[egg][floor] = float('inf')
            for k in range(1, floor + 1):
                # Drop egg from kth floor and check both cases (egg breaks and doesn't break)
                attempts = 1 + max(dp[egg - 1][k - 1], dp[egg][floor - k])
                dp[egg][floor] = min(dp[egg][floor], attempts)

    return dp[eggs][floors]


eggs_ex1 = int(input())
floors_ex1 = int(input())
result_ex1 = egg_drop(eggs_ex1, floors_ex1)
print(result_ex1)


