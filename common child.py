#We want to find the longest string that can be formed by removing characters from both strings without rearranging any letters. 
def common_child(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len_s1][len_s2]

input_s1_1 = input()
input_s2_1 = input()
output_1 = common_child(input_s1_1, input_s2_1)
print(output_1)


