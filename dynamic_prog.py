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
    res = []
    for x in range(len(c[-1])-1):
        if c[-1][x] < c[-1][x+1]:
            res.append(b[x])
    return res


def lis(a):
    """Longest increasing subsequence"""
    f = [0]*(len(a) + 1)
    for i in range(1, len(a) + 1):
        maximum = 0
        for j in range(i):
            if a[i-1] > a[j-1] and f[j] > maximum:
                maximum = f[j]
        f[i] = maximum + 1
    res = []
    i = f.index(max(f))
    while i:
        for j in range(1, i + 1):
            if f[i] - f[i-j] == 1:
                res.append(a[i-1])
                i = i - j
                break
    res.reverse()
    return res


if __name__ == '__main__':
    print(*lis('akbclmn'), sep='')

