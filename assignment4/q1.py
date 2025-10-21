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
    k = arr[-1]
    A = arr[:-1]

    P = {0}
    for a in A:
        P |= {p + a for p in P}

    return k in P


print(ArrayAdditionI(list(map(int, input().split()))))
