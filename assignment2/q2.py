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


def f(strParam: str) -> int:
    n, k = map(int, strParam.split())
    return hankerchief(n, k)


print(f(input()))
