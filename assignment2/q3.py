from collections import deque

ans: int = 0


def skip(Q: deque[int], k: int, i: int) -> None:
    if i < k - 1:
        Q.append(Q.popleft())
        skip(Q, k, i + 1)


def last_drop(Q: deque[int], k: int) -> None:
    if Q:
        skip(Q, k, 0)

        v = Q.popleft()
        if not Q:
            global ans
            ans = v
            return

        last_drop(Q, k)


def hankerchief(n: int, k: int) -> int:
    Q = deque(range(1, n + 1))
    last_drop(Q, k)
    return ans


def Throwhandkerchief(strParam: str) -> int:
    """
    >>> Throwhandkerchief("6 2")
    5
    >>> Throwhandkerchief("5 2")
    3
    >>> Throwhandkerchief("5 1")
    5
    >>> Throwhandkerchief("4 3")
    1
    >>> Throwhandkerchief("3 2")
    3
    >>> Throwhandkerchief("7 3")
    4
    >>> Throwhandkerchief("9 2")
    3
    >>> Throwhandkerchief("10 5")
    3
    >>> Throwhandkerchief("11 6")
    9
    >>> Throwhandkerchief("13 3")
    13
    """

    n, k = map(int, strParam.split())
    return hankerchief(n, k)


print(Throwhandkerchief(input()))
