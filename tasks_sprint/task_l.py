# L. Лишняя буква
# ID успешной посылки 65305442


from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    len_list = len(longer)
    len_sh = shorter.ljust(len_list, "~")
    sorted_shorter = sorted(len_sh)
    sorted_longer = sorted(longer)
    for i in range(0, len_list):
        if sorted_shorter[i] != sorted_longer[i]:
            return sorted_longer[i]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
