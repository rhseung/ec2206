from kit import sort_test


def my_insertion_sort(A: list[int]) -> list[int]:
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


def my_insertion_sort2(A: list[int]) -> list[int]:
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


sort_test(my_insertion_sort2)
