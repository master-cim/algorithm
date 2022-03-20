# I. Любители конференций
# ID успешной посылки
from collections import Counter
# from typing import List


def conference_lovers(id_university, k):
    number_participant = Counter(id_university)
    k_max = number_participant.most_common()[0:k:]
    result = [univer[0] for univer in k_max]

    print(' '.join(map(str, result)))


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


def quick_sort(start, end, array):
    if (start < end):
        part_index = partition(start, end, array)
        quick_sort(start, part_index - 1, array)
        quick_sort(part_index + 1, end, array)


# def print_array(result: List[int]):
#     print(' '.join(map(str, result)))


def read_input():
    number_students = int(input())
    id_university = [int(element) for element in input().strip().split()]
    k = int(input())
    start = 0
    end = number_students - 1
    quick_sort(start, end, id_university)
    return(id_university, k)


if __name__ == '__main__':
    id_university, k = read_input()
    conference_lovers(id_university, k)
