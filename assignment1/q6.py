def LetterCapitalize(strParam: str) -> str:
    """
    >>> LetterCapitalize("hello world")
    'Hello World'
    >>> LetterCapitalize("i love coding")
    'I Love Coding'
    >>> LetterCapitalize("h3llo yo people")
    'H3llo Yo People'
    >>> LetterCapitalize("yooooooo hi")
    'Yooooooo Hi'
    >>> LetterCapitalize("thisiscool")
    'Thisiscool'
    >>> LetterCapitalize("oxford comma")
    'Oxford Comma'
    >>> LetterCapitalize("letter by letter go")
    'Letter By Letter Go'
    >>> LetterCapitalize("a b c d e f")
    'A B C D E F'
    >>> LetterCapitalize("jelloupin here")
    'Jelloupin Here'
    """

    return ' '.join(map(lambda s: s.capitalize(), strParam.split(' ')))


# keep this function call here
print(LetterCapitalize(input()))
