from collections import defaultdict


def ArrayAdditionI(arr: list[int]) -> bool:
    """
    >>> ArrayAdditionI([4, 6, 23, 10, 1, 3])
    True
    >>> ArrayAdditionI([1, 2, 3, 4])
    True
    >>> ArrayAdditionI([2, 6, 18])
    False
    >>> ArrayAdditionI([10, 20, 30, 40, 100])
    True
    >>> ArrayAdditionI([10, 12, 500, 1, -5, 1, 0])
    False
    >>> ArrayAdditionI([-2, -3, -4, -1, 100])
    False
    >>> ArrayAdditionI([54, 49, 1, 0, 7, 4])
    True
    >>> ArrayAdditionI([3, 4, 5, 7])
    True
    >>> ArrayAdditionI([1, 1, 1, 1, 6])
    False
    >>> ArrayAdditionI([2, 4, 6, 12, 92])
    False
    >>> ArrayAdditionI([31, 2, 90, 50, 7])
    True
    """

    arr.sort()
    A = arr[:-1]
    k = arr[-1]

    DP = defaultdict(int)
    DP[0] = 1

    for a in A:
        K = list(DP.keys())
        for s in K:
            DP[s + a] += DP[s]

    return DP[k] > 0


print(ArrayAdditionI(list(map(int, input().split()))))
