# P. Частичная сортировка
# ID успешной посылки


def subtraction_items(square):
    while square != []:
        i = square.pop()
        for item in square:
            yield item - i


def partial_sorting(numb, arr):
    pr_less_bf = 0
    pr_big_bf = 0
    step = len(arr) - 1
    zerr_ar = 1
    print(arr)
    print(sorted(arr))
    print(arr[0], arr[1], arr[2], arr[3])
    while arr[step] != 0:
        if arr[step] < arr[step-1] and arr[step-1] == 0:
            pr_less_bf += 1
            step -= 1
        elif arr[step] > arr[step-1]:
            pr_big_bf += 1
            step -= 1
        elif arr[step] == 0:
            zerr_ar = 0
        else:
            break
    # print(pr_less_bf, pr_big_bf, zerr_ar)
    # print(pr_less_bf+pr_big_bf+zerr_ar)


def read_input():
    numb = int(input())
    arr = [int(element) for element in input().strip().split()]
    return numb, arr


if __name__ == '__main__':
    numb, arr = read_input()
    partial_sorting(numb, arr)
