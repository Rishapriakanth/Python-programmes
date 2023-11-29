#The problem is to determine the number of provinces in a given set of cities.
def findCircleNum(isConnected):
    def dfs(city):
        visited.add(city)
        for neighbor, connected in enumerate(isConnected[city]):
            if connected == 1 and neighbor not in visited:
                dfs(neighbor)

    n = len(isConnected)
    visited = set()
    provinces = 0

    for city in range(n):
        if city not in visited:
            provinces += 1
            dfs(city)

    return provinces

def get_user_input():
    n = int(input("Enter the number of cities: "))
    print("Enter the matrix isConnected (separate values by space):")
    isConnected = [list(map(int, input().split())) for _ in range(n)]
    return isConnected


isConnected_input = get_user_input()

output = findCircleNum(isConnected_input)
print("Number of provinces:", output)
