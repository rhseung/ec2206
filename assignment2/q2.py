def swapping(A: list[int], i: int, j: int) -> None:
    if j < i:
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
        swapping(A, i, j + 1)


def loop(A: list[int], i: int) -> None:
    if i > 0:
        swapping(A, i, 0)
        loop(A, i - 1)


def SortArrayusingrecursion(strParam: str) -> list[int]:
    """
    >>> SortArrayusingrecursion("8 9 10 2 4 5")
    [2, 4, 5, 8, 9, 10]
    >>> SortArrayusingrecursion("2 4 5 1 11 22 45")
    [1, 2, 4, 5, 11, 22, 45]
    >>> SortArrayusingrecursion("4 1 2 3 4 90 0")
    [0, 1, 2, 3, 4, 4, 90]
    >>> SortArrayusingrecursion("1 3 5 0 9 20 40")
    [0, 1, 3, 5, 9, 20, 40]
    >>> SortArrayusingrecursion("1 1 1 1 0 0 0")
    [0, 0, 0, 1, 1, 1, 1]
    >>> SortArrayusingrecursion("5 3 8 5 9 1 5")
    [1, 3, 5, 5, 5, 8, 9]
    >>> SortArrayusingrecursion("101 91 54 11 6 1")
    [1, 6, 11, 54, 91, 101]
    >>> SortArrayusingrecursion("-5 3 -2 4 0")
    [-5, -2, 0, 3, 4]
    >>> SortArrayusingrecursion("77 23 24 30 15")
    [15, 23, 24, 30, 77]
    >>> SortArrayusingrecursion("22 -8 45 99 10")
    [-8, 10, 22, 45, 99]
    """

    A = list(map(int, strParam.split()))
    loop(A, len(A) - 1)
    return A


print(SortArrayusingrecursion(input()))
