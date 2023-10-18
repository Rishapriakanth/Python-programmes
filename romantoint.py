def romantoint(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            result += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            result += roman[s[i]]
            i += 1
    return result
x = input()
print(romantoint(x))
