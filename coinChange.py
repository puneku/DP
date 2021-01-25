def coinChange(S,m,n):
    # do not include any coin
    if n == 0:
        return 1
    # no solution exists
    if n < 0:
        return 0
    if m<=0 and n >= 1:
        return 0
    return coinChange(S,m-1,n) + coinChange(S,m,n-S[m-1])

print(f'Brute Force solution  \n{coinChange([1,2,3],3,4)}')

def dpCoinChange(S,m,n):
    '''TC - O(n*m) and SC - O(n*m)'''
    dp = [[1 for _ in range(m)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(m):
            # count solutions with S[j]
            x = dp[i-S[j]][j] if i-S[j]>=0 else 0
            # count solutions without S[j]
            y = dp[i][j-1] if j>=1 else 0
            dp[i][j] = x + y
    return dp[n][m-1]
print(f"DP solution : First \n{dpCoinChange([1,2,3],3,4)}")