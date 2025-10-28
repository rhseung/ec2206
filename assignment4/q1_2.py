def ArrayAdditionI(arr):
    arr.sort()
    k = arr[-1]
    A = arr[:-1]

    DP = {0}
    for a in A:
        DP |= {p + a for p in DP}

    return k in DP


if __name__ == "__main__":
    print(ArrayAdditionI(list(map(int, input().split()))))
