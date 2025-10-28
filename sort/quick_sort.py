from kit import sort_test


def my_quick_sort(A: list[int], s: int, e: int) -> None:
    if s < e:
        p = my_partition(A, s, e)
        my_quick_sort(A, s, p - 1)
        my_quick_sort(A, p + 1, e)


def my_partition(A: list[int], s: int, e: int) -> int:
    p = s
    l, r = s + 1, e

    while l <= r:
        while l <= r and A[l] <= A[p]:
            l += 1

        while l <= r and A[p] <= A[r]:
            r -= 1

        if l < r:  # means A[l] > A[p] or A[p] > A[r]
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1

    A[p], A[r] = A[r], A[p]
    p, r = r, p

    return p


def my_quick_sort2(A: list[int], s: int, e: int):
    if s < e:
        p = my_partition2(A, s, e)
        my_quick_sort2(A, s, p - 1)
        my_quick_sort2(A, p + 1, e)


def my_partition2(A: list[int], s: int, e: int) -> int:
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


sort_test(my_quick_sort2)
