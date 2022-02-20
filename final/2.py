from typing import List, Tuple
import gc


def get_close_empty_section(n: int, section: List[int], ) -> List[int]:
    forward = [section[i:].index(0)
               if x != 0 else 0
               for i, x in enumerate(section)]
    section_r = section[::-1]
    backward = [section_r[j:].index(0)
                if 0 in section_r[j:] else 0
                if x == 0 else n
                for j, x in enumerate(section_r)][::-1]
    gc.collect()
    
    return [min(i, j) for i, j in zip(forward, backward)]


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, get_close_empty_section(n, section))))
