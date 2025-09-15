def ConsonantCount(strParam: str) -> int:
    """
    >>> ConsonantCount("Hello World")
    7
    >>> ConsonantCount("Alphabets")
    6
    >>> ConsonantCount("Development")
    7
    >>> ConsonantCount("Hewlett-Packard")
    10
    >>> ConsonantCount("here")
    2
    >>> ConsonantCount("www")
    3
    >>> ConsonantCount("w")
    1
    >>> ConsonantCount("hbhb")
    4
    >>> ConsonantCount("aaaaaaaa")
    0
    >>> ConsonantCount("zz*")
    2
    """

    ret = 0
    for c in strParam.lower():
        if c.isalpha():
            if c not in ['a', 'e', 'i', 'o', 'u']:
                ret += 1

    return ret


# keep this function call here
print(ConsonantCount(input()))
