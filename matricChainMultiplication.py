import sys


def matrix_chain_multi(p: list, i: int, j: int) -> int:
    if i == j:
        return 0
    _min = sys.maxsize
    for k in range(i, j):
        count = matrix_chain_multi(p, i, k) + matrix_chain_multi(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        _min = min(_min, count)
    return _min


p = [1, 2, 3, 4]
i = 1
j = len(p) - 1
print(f'Brute force recursive solution : {matrix_chain_multi(p, i, j)}')


def dp_matrix_chain_multiplication(p: list) -> int:
    # utility function for matrix multiplication
    def matrix_utility(p, i, j):
        dp = [[-1 for _ in range(len(p))] for _ in range(len(p))]
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        # sys.maxsize : largest possible value for an integer
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],
                           matrix_utility(p, i, k) + matrix_utility(p, k + 1, j) + p[i - 1] * p[k] * p[j]
                           )
        return dp[i][j]

    i, j = 1, len(p) - 1
    return matrix_utility(p, i, j)


print(f"minimum number of multiplications needed to multiply the chain : {dp_matrix_chain_multiplication([1, 2, 3, 4])}")
