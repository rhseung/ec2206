from kit import sort_test


def insertion_sort(A: list[int]) -> list[int]:
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


sort_test(insertion_sort)
