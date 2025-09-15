def SimpleAdding(num: str):
    """
    >>> SimpleAdding("45")
    1035
    >>> SimpleAdding("13")
    91
    >>> SimpleAdding("2")
    3
    >>> SimpleAdding("5")
    15
    >>> SimpleAdding("156")
    12246
    >>> SimpleAdding("999")
    499500
    >>> SimpleAdding("67")
    2278
    >>> SimpleAdding("123")
    7626
    >>> SimpleAdding("9")
    45
    >>> SimpleAdding("10")
    55
    """

    n = int(num)
    return n * (n + 1) // 2


# keep this function call here
print(SimpleAdding(input()))
