''' Given two strings str1 and str2 and below operations that can performed on str1.
    Find minimum number of edits (operations) required to convert str1 into str2.
        Insert
        Remove
        Replace
    All of the operations are of equal cost.'''

# brute force approach
def editDistance(str1,str2,m,n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    return 1 + min(editDistance(str1,str2,m,n-1),editDistance(str1,str2,m-1,n),editDistance(str1,str2,m-1,n-1))

str1 = "abcd"
str2 = "axyzbdc"

print(editDistance(str1,str2,len(str1),len(str2)))

# dp approach - first

def editDistanceDP(str1,str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], # Insert
                                   dp[i-1][j-1], # Replace
                                   dp[i][j-1]) # Remove
    return dp[m][n]

print(editDistanceDP(str1,str2))

