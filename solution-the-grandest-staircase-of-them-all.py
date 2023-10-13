def solution(n):
    dp=[1]+[0]*(n)
    for x in range(1, n+1):
        for y in range(n, x-1, -1):
            dp[y] += dp[y - x]
    return dp[-1]-1