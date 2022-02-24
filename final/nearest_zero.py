# A. Ближайший ноль
# ID успешной посылки 65358088
from typing import Tuple


def get_close_empty_section(cardinality: int, section: Tuple[int]):
    list_distance = [float('inf')] * cardinality
    for idx in [range(cardinality), range(cardinality-1, -1, -1)]:
        distance = float('inf')
        for i in idx:
            if section[i] == 0:
                distance = 0
            list_distance[i] = min(list_distance[i], distance)
            distance += 1
    return(list_distance)


def read_input() -> Tuple[int, Tuple[int]]:
    cardinality = int(input())
    section = [int(element) for element in input().strip().split()]
    return cardinality, section


if __name__ == '__main__':
    cardinality, section = read_input()
    print(*get_close_empty_section(cardinality, section), sep=' ')
