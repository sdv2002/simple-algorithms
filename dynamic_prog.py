import itertools
from pprint import pprint


def fib(n):
    """Finding Fibonacci number with dynamic programming. O(log n)"""
    a = [0, 1] + [None] * (n - 2)
    for i in range(2, n):
        a[i] = a[i - 1] + a[i - 2]
    return a


def number_of_trajectories(n, m):
    """Calculate the number of ways to get into the cell (n,m). O(n*m)"""
    a = [[0] * (m + 1) for _ in range(n + 1)]
    a[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            a[i][j] = a[i - 1][j] + a[i][j - 1]
    return a[-1][-1]


def lcs(a, b):
    """Longest common subsequence. O(n*m)"""
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
    """Longest increasing subsequence. O(n*m)"""
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


def levenshtein_distance(a, b):
    """String metric for measuring the difference between two sequences."""
    f = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)]
         for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[-1][-1]


def prefix(s):
    """The length of the longest prefix of a substring
    that is also the suffix of this substring. O(n)"""
    v = [0]*len(s)
    for i in range(1, len(s)):
        p = v[i-1]
        while p > 0 and s[p] != s[i]:
            p = v[p-1]
        if s[p] == s[i]:
            p = p + 1
        v[i] = p
    return v


def kmp(w, s):
    """Knuth–Morris–Pratt string-searching algorithm.
    This algorithm wants to find the starting index m in string s
    that matches the search word w. O(n)"""
    a = w + '#' + s
    p = prefix(a)
    if len(w) in p:
        m = p.index(len(w)) - 2 * len(w)
        return m


def knapsack_dynamic_prog(m, v, max_mass):
    """Knapsack problem. Given a set of items, each with a weight and a value,
    determine the number of each item to include in a collection so that
    the total weight is less than or equal to a given limit and
    the total value is as large as possible."""
    f = [[0] * (max_mass + 1) for _ in range(len(m) + 1)]
    for i in range(1, len(m) + 1):
        for j in range(1, max_mass + 1):
            if m[i-1] <= j:
                f[i][j] = max(f[i-1][j], v[i-1] + f[i-1][j - m[i-1]])
            else:
                f[i][j] = f[i-1][j]
    return f[-1][-1]


def knapsack_brute_force(m, v, max_mass):
    """Search for the highest value of items in a knapsack by brute force"""
    max_cost = 0
    for i in range(1, len(m) + 1):
        combinations = itertools.combinations(range(len(m)), i)
        for combination in combinations:
            set_cost = 0
            set_mass = 0
            for index in combination:
                set_cost += v[index]
                set_mass += m[index]
            if set_mass <= max_mass:
                if set_cost > max_cost:
                    max_cost = set_cost
    return max_cost


if __name__ == '__main__':
    masses = [1, 5, 7, 1]
    prices = [10, 20, 30, 15]
    pprint(knapsack_dynamic_prog(masses, prices, 7))
    print(knapsack_brute_force(masses, prices, 7))
