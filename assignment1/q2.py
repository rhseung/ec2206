from string import punctuation


def LongestWord(sen: str) -> str:
    """
    >>> LongestWord("hello world")
    'hello'
    >>> LongestWord("this is some sort of sentence")
    'sentence'
    >>> LongestWord("longest word!!")
    'longest'
    >>> LongestWord("a beautiful sentence^&!")
    'beautiful'
    >>> LongestWord("oxford press")
    'oxford'
    >>> LongestWord("123456789 98765432")
    '123456789'
    >>> LongestWord("letter after letter!!")
    'letter'
    >>> LongestWord("a b c dee")
    'dee'
    >>> LongestWord("a confusing /:sentence:/[ this is not!!!!!!!~")
    'confusing'
    """

    max_len = 0
    max_word = ''
    sen = sen.translate(str.maketrans(dict.fromkeys(punctuation)))

    for word in sen.split(' '):
        if len(word) > max_len:
            max_len = len(word)
            max_word = word

    return max_word


print(LongestWord(input()))
