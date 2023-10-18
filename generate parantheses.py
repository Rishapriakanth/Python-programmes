#GENERATE PARENTHESES

def generate_parentheses(n):
    result = []
    backtrack('', 0, 0, n, result)
    return result


def backtrack(current, open_count, close_count, n, result):
    if len(current) == 2 * n:
        result.append(current)
        return

    if open_count < n:
        backtrack(current + '(', open_count + 1, close_count, n, result)
    if close_count < open_count:
        backtrack(current + ')', open_count, close_count + 1, n, result)


n = int(input())
output = generate_parentheses(n)
for i in output:
    print(i)
