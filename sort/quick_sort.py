from kit import sort_test


def quick_sort(A: list[int], s: int, e: int) -> None:
    if s < e:
        p = partition(A, s, e)
        quick_sort(A, s, p - 1)
        quick_sort(A, p + 1, e)


def partition(A: list[int], s: int, e: int) -> int:
    p = s
    l, r = s + 1, e

    while l <= r:
        while l <= r and A[l] <= A[p]:
            l += 1

        while l <= r and A[p] <= A[r]:
            r -= 1

        if l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1

    A[p], A[r] = A[r], A[p]
    p, r = r, p

    return p


sort_test(quick_sort)
