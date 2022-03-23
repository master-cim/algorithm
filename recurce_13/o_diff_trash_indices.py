# O. Разность треш-индексов
# ID успешной посылки


def diff_index(numb, square, k_position):
    print(k_position)
    d = 0
    numb = numb - 1
    while numb >= 1:
        d += numb
        numb -= 1
    print(d)
    diff = [''] * d
    idx = 0
    while square != []:
        i = square.pop()
        for j in square:
            diff[idx] = abs(j-i)
            idx += 1
    print(diff)
    print(sorted(diff))
    print(diff[2])
    return(diff[k_position-1])


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    print(diff_index(numb, square, k_position))
