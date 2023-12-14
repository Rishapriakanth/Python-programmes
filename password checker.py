def check_passwords(passwords):
    n = len(passwords)
    for i in range(n):
        for j in range(i + 1, n):
            if passwords[i] == passwords[j]:
                continue  # Skip identical passwords
            min_len = min(len(passwords[i]), len(passwords[j]))
            if passwords[i][:min_len] == passwords[j][:min_len]:
                return 'BAD PASSWORD'
    return 'GOOD PASSWORD'

user_input_1 = input()
passwords1 = user_input_1.split()
result1 = check_passwords(passwords1)
print(result1)

