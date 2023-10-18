# longest substring with unique characters
def longest_substring(s):
    unique_character = set()
    start = 0
    max_length = 0
    for end in range(len(s)):
        while s[end] in unique_character:
            unique_character.remove(s[start])
            start += 1
        unique_character.add(s[end])
        max_length = max(max_length, end - start + 1)
    return max_length


s = input()
output = longest_substring(s)
print(output)
