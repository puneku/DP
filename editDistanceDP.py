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
