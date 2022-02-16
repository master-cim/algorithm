from typing import List, Tuple


def modulo(arr) -> Tuple[int, int]:
    count_p = 0
    count_n = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            count_p += 1
        else:
            count_n += 1
    if count_p == 3 or count_n == 3:
        print('WIN')
    else:
        print('FAIL')


def read_input() -> List[int]:
    arr = list(map(int, input().strip().split()))
    return arr


arr = read_input()
modulo(arr)