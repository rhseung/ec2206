def WaveSorting(arr: list[int]) -> bool:
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

    # 배열의 길이를 n이라고 할 때 [a_1, a_2, a_3, ..., a_n]을 오름차순 정렬했을 때 [L_1, L_2, ..., L_{n/2}, H_1, H_2, ..., H_{n/2}]이라 하자. (홀짝 무시)
    # 이러면, H_1 > L_1 < H_2 > L_2 < H_3 > ... < H_{n/2 - 1} > L_{n/2 - 1} < H_{n/2} > L_{n/2} (< H_{n/2 + 1}) 으로 항상 wave sort할 수 있음. (n이 홀수인 경우, H가 1개 더 많아도 됨)
    # 여기서 불가능한 경우는 임의의 자연수 i에 대해 H_i <= L_i일 경우 wave sort가 불가능함.

    arr.sort()
    n = len(arr)
    m = n // 2

    for i in range(n - m):
        if arr[i] >= arr[i + m]:
            return False

    return True


print(WaveSorting(list(map(int, input().split()))))
