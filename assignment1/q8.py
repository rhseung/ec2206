def NumberReverse(strParam: str) -> str:
    """
    >>> NumberReverse("1 2 3")
    '3 2 1'
    >>> NumberReverse("10 20 50")
    '50 20 10'
    >>> NumberReverse("100 200 34")
    '34 200 100'
    >>> NumberReverse("2 3 1000000")
    '1000000 3 2'
    >>> NumberReverse("123123 2323423 23423412")
    '23423412 2323423 123123'
    >>> NumberReverse("23 23 23 566 76")
    '76 566 23 23 23'
    """

    return ' '.join(strParam.split(' ')[::-1])


# keep this function call here
print(NumberReverse(input()))
