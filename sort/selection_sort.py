from kit import sort_test


def my_selection_sort(A: list[int]) -> list[int]:
    for i in range(len(A) - 1):
        min_i = i
        for j in range(i + 1, len(A)):
            if A[min_i] > A[j]:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]

    return A


def my_selection_sort2(A: list[int]) -> list[int]:
    n = len(A)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if A[min_i] > A[j]:
                min_i = j
        A[min_i], A[i] = A[i], A[min_i]
        
    return A


sort_test(my_selection_sort2)
