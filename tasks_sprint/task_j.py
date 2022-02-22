# J. Факторизация
# ID успешной посылки 65303761

from typing import List


def factorize(number: int) -> List[int]:
    i = 2
    result = []
    while i * i <= number:
        while number % i == 0:
            result.append(i)
            number = int(number / i)
        i = i + 1
    if number > 1:
        result.append(number)
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))
