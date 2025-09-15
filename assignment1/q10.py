def CodelandUsernameValidation(strParam: str) -> bool:
    """
    >>> CodelandUsernameValidation("aaaaaaaaaa")
    True
    >>> CodelandUsernameValidation("aa_")
    False
    >>> CodelandUsernameValidation("u__hello_world123")
    True
    >>> CodelandUsernameValidation("_")
    False
    >>> CodelandUsernameValidation("__bbbbbbb")
    False
    >>> CodelandUsernameValidation("b3333434_")
    False
    >>> CodelandUsernameValidation("usernamehello123")
    True
    >>> CodelandUsernameValidation("oooooooooooooooooo________a")
    False
    >>> CodelandUsernameValidation("123abc444")
    False
    >>> CodelandUsernameValidation("a______b_________555555555555aaaa")
    False
    """

    if not 4 <= len(strParam) <= 25:
        return False
    elif not strParam[0].isalpha():
        return False
    elif strParam[-1] == '_':
        return False

    for c in strParam:
        if not (c.isalnum() or c == '_'):
            return False

    return True


# keep this function call here
print(CodelandUsernameValidation(input()))
