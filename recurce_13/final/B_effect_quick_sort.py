# B. Эффективная быстрая сортировка
# ID успешной посылки 66235845


def partition(competitors, left, right):
    pivot_competitors = (competitors[left])
    start = left + 1
    end = right - 1
    while True:
        if (start <= end and competitors[end] > pivot_competitors):
            end -= 1
        elif (start <= end and competitors[start] < pivot_competitors):
            start += 1
        elif ((competitors[end] > pivot_competitors)
              or (competitors[start] < pivot_competitors)):
            continue
        if start <= end:
            competitors[start], competitors[end] = (competitors[end],
                                                    competitors[start])
        else:
            competitors[left], competitors[end] = (competitors[end],
                                                   competitors[left])
            return end


def quick_sort(competitors, left, right):
    if ((right - left) > 1):
        pivot = partition(competitors, left, right)
        quick_sort(competitors, left, pivot)
        quick_sort(competitors, pivot + 1, right)


def transform_array(competitors):
    competitors[1] = - int(competitors[1])
    competitors[2] = int(competitors[2])
    return [competitors[1], competitors[2], competitors[0]]


def read_input():
    number = int(input())
    competitors = [transform_array(input().split()) for _ in range(number)]
    return(competitors, number)


if __name__ == '__main__':
    competitors, number = read_input()
    left = 0
    quick_sort(competitors, left, number)
    print(*(list(zip(*competitors))[2]), sep="\n")
