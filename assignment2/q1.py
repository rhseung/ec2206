def swapping(A: list[int], i: int, j: int) -> None:
    if j < i:
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
        swapping(A, i, j + 1)


def loop(A: list[int], i: int) -> None:
    if i > 0:
        swapping(A, i, 0)
        loop(A, i - 1)


def f(strParam: str) -> list[int]:
    A = list(map(int, strParam.split()))
    loop(A, len(A) - 1)
    return A


print(f(input()))
