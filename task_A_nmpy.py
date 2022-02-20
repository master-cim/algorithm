from typing import List, Tuple
import numpy as np


def get_close_empty_section(n: int, section: Tuple[int], ) -> List[int]:
    list_zero_index = np.array([idx for idx, x in enumerate(section) if x == 0])
    print(list_zero_index)
    distances = [min(abs(idx-np.array(list_zero_index))) for idx, x in enumerate(section)]
    return distances


def read_input() -> Tuple[int, Tuple[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, get_close_empty_section(n, section))))
