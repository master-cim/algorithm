# ID успешной посылки 65358088
from typing import List, Tuple


def get_close_empty_section(n: int, section: Tuple[int]) -> List[int]:
    list_distance = [float('inf')] * n
    for idx in [range(n), range(n-1, -1, -1)]:
        distance = float('inf')
        for i in idx:
            if section[i] == 0:
                distance = 0
            list_distance[i] = min(list_distance[i], distance)
            distance += 1
    return(list_distance)


def read_input() -> Tuple[int, Tuple[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, get_close_empty_section(n, section))))
