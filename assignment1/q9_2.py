def make_next_number(n):
    ret = 0
    while n != 0:
        ret += (n % 10) ** 2
        n //= 10

    return ret


seen = set()


def HappyNumbers(num):
    """
    >>> HappyNumbers(1)
    True
    >>> HappyNumbers(2)
    False
    >>> HappyNumbers(10)
    True
    >>> HappyNumbers(100)
    True
    >>> HappyNumbers(101)
    False
    >>> HappyNumbers(0)
    False
    >>> HappyNumbers(5525)
    True
    >>> HappyNumbers(5255)
    True
    >>> HappyNumbers(2555)
    True
    >>> HappyNumbers(5552)
    True
    """

    # print(num, seen)

    if num == 1:
        return True
    elif num in seen:
        return False

    seen.add(num)
    num_next = make_next_number(num)
    return HappyNumbers(num_next)


if __name__ == "__main__":
    print(HappyNumbers(int(input())))
