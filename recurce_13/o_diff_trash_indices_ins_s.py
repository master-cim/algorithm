# O. Разность треш-индексов
# ID успешной посылки


def diff_index(square):
    diff = []
    while square != []:
        i = square.pop()
        for j in square:
            diff.append(abs(j-i))
    return(diff)


def insertion_sort(diff):
    for i in range(1, len(diff)):
        item_to_insert = diff[i]
        j = i - 1
        while j >= 0 and diff[j] > item_to_insert:
            diff[j + 1] = diff[j]
            j -= 1
        diff[j + 1] = item_to_insert


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(square)
    insertion_sort(diff)
    print(diff[k_position-1])

