def partition(competitors, left, right):
    pivot = (competitors[left])
    i = left + 1
    j = right - 1
    while True:
        if (i <= j and competitors[j] > pivot):
            j -= 1
        elif (i <= j and competitors[i] < pivot):
            i += 1
        elif (competitors[j] > pivot) or (competitors[i] < pivot):
            continue
        if i <= j:
            competitors[i], competitors[j] = competitors[j], competitors[i]
        else:
            competitors[left], competitors[j] = competitors[j], competitors[left]
            return j
def quick_sort(competitors, left, right):
    if ((right - left) > 1):
        p = partition(competitors, left, right)
        quick_sort(competitors, left, p)
        quick_sort(competitors, p + 1, right)
def transformation(competitors):
    competitors[1] = - int(competitors[1])
    competitors[2] = int(competitors[2])
    return [competitors[1], competitors[2], competitors[0]]
if __name__ == '__main__':
    number = int(input())
    competitors = [transformation(input().split()) for _ in range(number)]
    left = 0
    quick_sort(competitors, left, len(competitors))
    print(*(list(zip(*competitors))[2]), sep="\n")