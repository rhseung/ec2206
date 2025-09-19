from collections import deque


def RemoveBrackets(strParam: str) -> int:
    """
    >>> RemoveBrackets("(()))")
    1
    >>> RemoveBrackets("(())()(((")
    3
    >>> RemoveBrackets("(()(")
    2
    >>> RemoveBrackets("()")
    0
    >>> RemoveBrackets(")(()")
    2
    >>> RemoveBrackets("((()))")
    0
    >>> RemoveBrackets("()()()()()()()()((((((")
    6
    >>> RemoveBrackets(")(()")
    2
    >>> RemoveBrackets("((()))()()(()))")
    1
    >>> RemoveBrackets(")(())")
    1
    """

    stack = deque()
    for c in strParam:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)

    return len(stack)


# keep this function call here
print(RemoveBrackets(input()))
