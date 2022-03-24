# O. Разность треш-индексов
# ID успешной посылки


def diff_index(numb, square):
    diff = [''] * (numb * (numb-1) // 2)
    idx = 0
    while square != []:
        i = square.pop()
        for j in square:
            diff[idx] = abs(j-i)
            idx += 1
    return(diff)


def get_position(arr, k_position):
    arr.sort()
    return(arr[k_position-1])


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    print(get_position(diff_index(numb, square), k_position))


