def fib(n):
    """Finding Fibonacci number with dynamic programming"""
    a = [0, 1] + [None] * (n - 2)
    for i in range(2, n):
        a[i] = a[i - 1] + a[i - 2]
    return a


def number_of_trajectories(n, m):
    """Calculate the number of ways to get into the cell (n,m)"""
    a = [[0] * (m + 1) for _ in range(n + 1)]
    a[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            a[i][j] = a[i - 1][j] + a[i][j - 1]
    return a[-1][-1]


def lcs(a, b):
    """Longest common subsequence."""
    c = [[0]*(len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[-1][-1]



if __name__ == '__main__':
    print(lcs('abcdrrrrr', 'acsd'))
