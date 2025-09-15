def LetterChanges(strParam: str) -> str:
    """
    >>> LetterChanges("hello world")
    'Ifmmp xpsmE'
    >>> LetterChanges("sentence")
    'tfOUfOdf'
    >>> LetterChanges("replace!*")
    'sfqmbdf!*'
    >>> LetterChanges("coderbyte")
    'dpEfsczUf'
    >>> LetterChanges("beautiful^")
    'cfbvUjgvm^'
    >>> LetterChanges("oxford")
    'pygpsE'
    >>> LetterChanges("123456789ae")
    '123456789bf'
    >>> LetterChanges("this long cake@&")
    'UIjt mpOh dblf@&'
    >>> LetterChanges("a b c dee")
    'b c d Eff'
    >>> LetterChanges("a confusing /:sentence:/[ this is not!!!!!!!~")
    'b dpOgvtjOh /:tfOUfOdf:/[ UIjt jt OpU!!!!!!!~'
    """

    ret = ''

    for c in strParam:
        if 'a' <= c <= 'z':
            c2 = chr(ord(c) + 1)
            if c2 == 'a' or c2 == 'e' or c2 == 'i' or c2 == 'o' or c2 == 'u':
                c2 = c2.capitalize()
            ret += c2
        else:
            ret += c

    return ret


print(LetterChanges(input()))
