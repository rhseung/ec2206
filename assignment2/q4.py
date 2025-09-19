def StringPeriods(strParam: str) -> str | int:
    """
    >>> StringPeriods("abcababcababcab")
    'abcab'
    >>> StringPeriods("abababababab")
    'ababab'
    >>> StringPeriods("abcxabc")
    -1
    >>> StringPeriods("affedaaffed")
    -1
    >>> StringPeriods("f")
    -1
    >>> StringPeriods("gg")
    'g'
    >>> StringPeriods("aaaaacccccacacaaaaacccccacac")
    'aaaaacccccacac'
    >>> StringPeriods("aaaaaaaaaa")
    'aaaaa'
    >>> StringPeriods("abcabcabc")
    'abc'
    >>> StringPeriods("tttttttrtttttttrtttttttrtttttttr")
    'tttttttrtttttttr'
    """

    n = len(strParam)
    for k in range(n // 2, 0, -1):
        if n % k == 0:
            maybe = strParam[:k]
            if maybe * (n // k) == strParam:
                return maybe
    return -1


# keep this function call here
print(StringPeriods(input()))
