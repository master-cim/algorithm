# A. Генератор скобок
# ID успешной посылки 66101670


def bubble_sort(len_arr, arr):
    flag = 1
    for i in range(len_arr - 1):
        for j in range(0, len_arr-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 1:
            for x in arr:
                print(x, end=' ')
            print('')
            flag = 0


def read_input():
    len_arr = int(input())
    arr = [int(element) for element in input().strip().split()]
    return(len_arr, arr)


if __name__ == '__main__':
    len_arr, arr = read_input()
    bubble_sort(len_arr, arr)
