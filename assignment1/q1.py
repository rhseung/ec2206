def FirstFactorial(num: str) -> int:
    """
    >>> FirstFactorial("3")
    6
    >>> FirstFactorial("4")
    24
    >>> FirstFactorial("5")
    120
    >>> FirstFactorial("6")
    720
    >>> FirstFactorial("7")
    5040
    >>> FirstFactorial("8")
    40320
    >>> FirstFactorial("9")
    362880
    >>> FirstFactorial("10")
    3628800
    """

    n = int(num)
    ret = 1
    while n > 0:
        ret *= n
        n -= 1

    return ret


print(FirstFactorial(input()))
