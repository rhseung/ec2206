from kit import sort_test


def my_merge_sort(A: list[int], s: int, e: int) -> None:
    if s < e:
        m = (s + e) // 2
        my_merge_sort(A, s, m)
        my_merge_sort(A, m + 1, e)
        my_merge(A, s, m, e)


def my_merge(A: list[int], s: int, m: int, e: int) -> None:
    L = A[s:m + 1]
    R = A[m + 1:e + 1]

    n_L, n_R = len(L), len(R)

    i, l, r = s, 0, 0

    while l < n_L and r < n_R:
        if L[l] <= R[r]:
            A[i] = L[l]
            l += 1
        else:
            A[i] = R[r]
            r += 1
        i += 1

    while l < n_L:
        A[i] = L[l]
        l += 1
        i += 1

    while r < n_R:
        A[i] = R[r]
        r += 1
        i += 1


def my_merge_sort2(A: list[int], s: int, e: int):
    if s < e:
        m = (s + e) // 2
        my_merge_sort(A, s, m)
        my_merge_sort(A, m + 1, e)
        my_merge2(A, s, m, e)


def my_merge2(A: list[int], s: int, m: int, e: int):
    L = A[s:m + 1]
    R = A[m + 1:e + 1]

    n_L, n_R = len(L), len(R)
    l, r = 0, 0
    i = s

    while l < n_L and r < n_R:
        if L[l] <= R[r]:
            A[i] = L[l]
            l += 1
        else:
            A[i] = R[r]
            r += 1
        i += 1

    while l < n_L:
        A[i] = L[l]
        i += 1
        l += 1

    while r < n_R:
        A[i] = R[r]
        i += 1
        r += 1


sort_test(my_merge_sort2)
