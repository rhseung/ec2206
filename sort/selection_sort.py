from kit import sort_test


def selection_sort(A: list[int]) -> list[int]:
    for i in range(len(A) - 1):
        min_i = i
        for j in range(i + 1, len(A)):
            if A[min_i] > A[j]:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]

    return A


sort_test(selection_sort)
