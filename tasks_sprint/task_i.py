# I. Степень четырёх
# ID успешной посылки 65303331


import math


def is_power_of_four(number: int) -> bool:
    log = math.log(number, 4)
    if int(log * 100) % 100 == 0:
        return 'True'
    else:
        return 'False'

print(is_power_of_four(int(input())))
