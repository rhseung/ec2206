from kit import sort_test


def merge_sort(A: list[int], s: int, e: int) -> None:
    if s < e:
        m = (s + e) // 2
        merge_sort(A, s, m)
        merge_sort(A, m + 1, e)
        merge(A, s, m, e)


def merge(A: list[int], s: int, m: int, e: int) -> None:
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


sort_test(merge_sort)
