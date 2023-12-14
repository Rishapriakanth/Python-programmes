#You are given a string representing an integer and a maximum number of changes you can make. Your goal is to modify the string, one digit at a time, to create the highest possible integer while adhering to the constraint on the number of changes.netwro
def largest_palindrome(num_changes, num_str):
    num_str = list(num_str)
    length = len(num_str)

    mismatches_count = sum([num_str[i] != num_str[length - 1 - i] for i in range(length // 2)])

    for i in range(length // 2):
        left_digit = int(num_str[i])
        right_digit = int(num_str[length - 1 - i])

        if left_digit != right_digit:
            max_digit = max(left_digit, right_digit)
            num_str[i] = str(max_digit)
            num_str[length - 1 - i] = str(max_digit)
            num_changes -= 1

    middle_index = length // 2
    if num_changes > 0 and num_str[middle_index] != '9':
        num_str[middle_index] = '9'
        num_changes -= 1

    i = 0
    while num_changes > 0 and i < length // 2:
        if num_str[i] != '9':
            num_str[i] = '9'
            num_str[length - 1 - i] = '9'
            num_changes -= 2
        i += 1

    return ''.join(num_str)


input_changes_1 = int(input())
input_num_1 = input()
output_1 = largest_palindrome(input_changes_1, input_num_1)
print(output_1)

