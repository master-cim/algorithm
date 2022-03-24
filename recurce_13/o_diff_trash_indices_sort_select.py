# O. Разность треш-индексов
# ID успешной посылки


def diff_index(square):
    diff = []
    while square != []:
        i = square.pop()
        for j in square:
            diff.append(abs(j-i))
    return(diff)


def select_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[min_index] > lst[j]:
                min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(square)
    print(diff)
    select_sort(diff)
    print(diff)
    print(diff[k_position-1])


