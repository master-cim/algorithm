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


def shell_sort(lst):
    def shell_insert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i-d
            temp = arr[i]
            while (j >= 0 and arr[j] > temp):
                arr[j + d] = arr[j]
                j -= d
            if j != i-d:
                arr[j+d] = temp
    n = len(lst)
    if n <= 1:
        return lst
    d = n//2
    while d >= 1:
        shell_insert(lst, d)
        d = d // 2
    return lst


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(numb, square)
    shell_sort(diff)
    print(diff[k_position-1])

