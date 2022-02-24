# B. Ловкость рук
# ID успешной посылки 65406475
from typing import List, Tuple


def twist_of_the_wrist(number_keys: int, matrix: List[str]) -> int:
    limit_pressures = number_keys * 2
    count_numbers = dict((number, matrix.count(number))
                         for number in set(matrix)
                         if matrix.count(number) > 0)
    win = 0
    pairs = [(sum_numbers, number_keys)
             for (number_keys, sum_numbers) in count_numbers.items()]
    for i in range(0, len(count_numbers)):
        if pairs[i][0] <= limit_pressures:
            win += 1
    print(win)


def read_input() -> Tuple[int, List[List[str]]]:
    number_keys = int(input())
    matrix = []
    for _ in range(4):
        matrix.extend([element for element in input().strip()
                       if element != '.'])
    return number_keys, matrix


if __name__ == '__main__':
    number_keys, matrix = read_input()
    twist_of_the_wrist(number_keys, matrix)
