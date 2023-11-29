def repeatedStringMatch(a, b):
    # Check if b is already a substring of a
    if b in a:
        return 1

    # Repeat a until its length is greater than or equal to the length of b
    repeated_a = a
    count = 1

    while len(repeated_a) < len(b):
        repeated_a += a
        count += 1

    # Check if b is now a substring of the repeated a
    if b in repeated_a:
        return count
    elif b in repeated_a + a:
        return count + 1
    else:
        return -1

a1 = input()
b1 = input()
result1 = repeatedStringMatch(a1, b1)
print("Minimum number of times to repeat 'a':", result1)
