
MAX_VAL = 999999

# Brute Force approach

def minCostPath(arr,m,n):
    if m<0 or n<0:
        return MAX_VAL
    if m==0 and n==0:
        return arr[m][n]
    else:
        return arr[m][n] + min(
            minCostPath(arr,m-1,n-1),
            minCostPath(arr,m-1,n),
            minCostPath(arr,m,n-1)
        )

arr = [[i for i in range(1,4)],[i for i in range(2,5)],[i for i in range(3,6)]]
m = 2
n = 1
print(arr)
print(minCostPath(arr,m,n))

# Dp approach - 1
# TC - O(m*n) SC -O(m*n)

def dpMinCostPath(mat,m,n):
    # dp[m+1][n+1]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = mat[0][0]
    # fill first column
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] + mat[i][0]
    # fill first row
    for j in range(1,n+1):
        dp[0][j] = dp[0][j-1] + mat[0][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + mat[i][j]
    return dp[m][n]

print(dpMinCostPath(arr,m,n))

# Dp Approach - 2
# TC -O(m*n)

def dptwoMinCostPath(mat, m,n):
    # fill first row
    for i in range(1,n+1):
        mat[0][i] += mat[0][i-1]
    # fill first column
    for j in range(1,m+1):
        mat[j][0] += mat[j-1][0]
    # fill remaining matrix
    for i in range(1,m+1):
        for j in range(1,n+1):
            mat[i][j] += min( mat[i-1][j-1],
                              mat[i-1][j],
                              mat[i][j-1]
                              )
    return mat[m][n]

print(dptwoMinCostPath(arr,m,n))