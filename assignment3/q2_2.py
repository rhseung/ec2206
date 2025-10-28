def sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def WaveSorting(arr):
    """
    >>> WaveSorting([0, 1, 2, 4, 1, 4])
    True
    >>> WaveSorting([0, 1, 2, 4, 1, 1, 1])
    False
    >>> WaveSorting([0, 4, 22, 4, 14, 4, 2])
    True
    >>> WaveSorting([1, 1, 1])
    False
    >>> WaveSorting([0, 67])
    True
    >>> WaveSorting([0, 1, 2, 3, 3, 3, 3, 3, 8, 9])
    True
    >>> WaveSorting([10, 90, 49, 2, 1, 5, 23])
    True
    >>> WaveSorting([10, 90, 49, 2, 1, 5, 23, 45, 21, 22])
    True
    >>> WaveSorting([1, 1, 1, 1, 5, 2, 5, 1, 1, 3, 5, 6, 8, 3])
    True
    >>> WaveSorting([10, 100, 20, 300])
    True
    """

    sort(arr)
    n = len(arr)

    for i in range(n - n // 2):
        if arr[i] >= arr[i + n // 2]:
            return False

    return True


if __name__ == "__main__":
    print(WaveSorting(list(map(int, input().split()))))
