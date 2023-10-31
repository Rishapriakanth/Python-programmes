#Tower Breakers is a game played between two players, where the first move is always made by Player 1.
# The game revolves around a set of towers with varying heights.

def tower_breakers(n, m):
    if n == 1:# If there's only one tower, Player 1 wins.
        return 1
    if m == 1:# If any tower's height is 1, Player 1 wins.
        return 1
    if m % 2 == 0: # If any tower's height is even, Player 2 wins.
        return 2
    return 1

n = int(input())
m = int(input())
result = tower_breakers(n, m)
print(result)
