# D. Печеньки
# ID успешной посылки 66170829


def biscuits(factor, sizes):
    happy_child = 0
    for i in range(len(factor)):
        if sizes and factor[i] <= sizes[-1]:
            sizes.pop()
            happy_child += 1
    return(happy_child)


def read_input():
    _ = int(input())
    factor = sorted(list(map(int, input().split())), reverse=True)
    _ = int(input())
    sizes = sorted(list(map(int, input().split())))
    return factor, sizes


if __name__ == '__main__':
    factor, sizes = read_input()
    print(biscuits(factor, sizes))
