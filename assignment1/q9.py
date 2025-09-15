seen = set()


def HappyNumbers(num: str) -> bool:
    """
    >>> HappyNumbers("1")
    True
    >>> HappyNumbers("2")
    False
    >>> HappyNumbers("10")
    True
    >>> HappyNumbers("100")
    True
    >>> HappyNumbers("101")
    False
    >>> HappyNumbers("0")
    False
    >>> HappyNumbers("5525")
    True
    >>> HappyNumbers("5255")
    True
    >>> HappyNumbers("2555")
    True
    >>> HappyNumbers("5552")
    True
    """

    n = int(num)
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n in seen:
        return False

    def sum_sq(x: int) -> int:
        r = 0
        while x > 0:
            r += (x % 10) ** 2
            x //= 10

        return r

    ret = sum_sq(n)

    if ret == 1:
        seen.clear()
        return True
    else:
        seen.add(n)
        return HappyNumbers(str(ret))


# keep this function call here
print(HappyNumbers(input()))
