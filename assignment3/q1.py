def SecondGreatLow(arr: list[int]) -> str:
    """
    >>> SecondGreatLow([1, 2, 2, 3])
    '2 2'
    >>> SecondGreatLow([2, 2, 2, 5, 5, 5, 6])
    '5 5'
    >>> SecondGreatLow([100, 30, 6])
    '30 30'
    >>> SecondGreatLow([78, 90, 100, 1, 2])
    '2 90'
    >>> SecondGreatLow([-4, -5, 10, 2])
    '-4 2'
    >>> SecondGreatLow([100, 200, 3, 400, 5, 1])
    '3 200'
    >>> SecondGreatLow([4, 60, 7, 188])
    '7 60'
    >>> SecondGreatLow([80, 80])
    '80 80'
    >>> SecondGreatLow([90, 23])
    '90 23'
    >>> SecondGreatLow([7, 7, 90, 1000003])
    '90 90'
    """

    uniq = list(set(arr))
    uniq.sort()

    if len(uniq) >= 2:
        return f"{uniq[1]} {uniq[-2]}"
    else:
        return f"{uniq[0]} {uniq[0]}"


print(SecondGreatLow(list(map(int, input().split()))))
