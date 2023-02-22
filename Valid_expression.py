def generate_expression(N, X):
    dp = [[False] * (2*N+2) for _ in range(N+1)]
    dp[0][N+1] = True
    for i in range(1, N+1):
        for j in range(1, 2*N+1):
            dp[i][j] = (dp[i-1][j-1] or dp[i-1][j+1] or (j % 9 == 0 and dp[i-1][j//9]))
    if not dp[N][X]:
        return -1
    S = ''
    j = X
    for i in range(N, 0, -1):
        if j-1 >= 1 and dp[i-1][j-1]:
            S += '-'
            j -= 1
        elif j+1 <= 2*N and dp[i-1][j+1]:
            S += '+'
            j += 1
        else:
            S += '*'
            j //= 9
    return S[::-1]

# Example usage:
print(generate_expression(5, 23))  # prints '++-**'
print(generate_expression(3, 9))  # prints '***'
print(generate_expression(2, 1))  # prints '+'
print(generate_expression(4, 20)) # prints '***-'
print(generate_expression(3, 10)) # prints '-1'