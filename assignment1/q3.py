def FirstReverse(strParam: str) -> str:
    """
    >>> FirstReverse("Coderbyte")
    'etybredoC'
    >>> FirstReverse("I Love Coding")
    'gnidoC evoL I'
    >>> FirstReverse("h333llLo")
    'oLll333h'
    >>> FirstReverse("Yo0")
    '0oY'
    >>> FirstReverse("thisiscool")
    'loocsisiht'
    >>> FirstReverse("commacomma!")
    '!ammocammoc'
    >>> FirstReverse("123456789")
    '987654321'
    >>> FirstReverse("lettersz!23z")
    'z32!zsrettel'
    >>> FirstReverse("aq")
    'qa'
    """

    return strParam[::-1]


# keep this function call here
print(FirstReverse(input()))
