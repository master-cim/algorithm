# A. Генератор скобок
# ID успешной посылки 66098296

COMBINATIONS = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }


def gen_combination(digits, prefix, result):
    if digits == '':
        result.append(prefix)
        return
    for letter in COMBINATIONS[digits[0]]:
            prefix += letter
            gen_combination(digits[1:], prefix, result)
            prefix = prefix[:-1]


def read_input():
    digits = input()
    return digits


if __name__ == '__main__':
    result = []
    digits = read_input()
    gen_combination(digits, '', result)
    for x in result:
        print(x, end=' ')
