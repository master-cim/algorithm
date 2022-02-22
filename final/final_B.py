# B. Ловкость рук
# ID успешной посылки 65406475
from typing import List, Tuple


def twist_of_the_wrist(k: int, matrix: List[str]) -> int:
    limit_pressures = k * 2
    count_numbers = dict((x, matrix.count(x))
                         for x in set(matrix)
                         if matrix.count(x) > 0)
    win = 0
    pairs = [(v, k) for (k, v) in count_numbers.items()]
    for i in range(0, len(count_numbers)):
        if pairs[i][0] <= limit_pressures:
            win += 1
    print(win)


def read_input() -> Tuple[int, List[List[str]]]:
    k = int(input())
    matrix = []
    for _ in range(4):
        matrix.extend(list(map(str, input().strip())))
    matrix = [n for n in matrix if n != '.']
    return k, matrix


k, matrix = read_input()
twist_of_the_wrist(k, matrix)
