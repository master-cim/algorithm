# A. Генератор скобок
# ID успешной посылки 66033244


def brackets(list_brackets, n):
    if(n > 0):
        brackets_generatior(list_brackets, 0,
                            n, 0, 0)
    return


def brackets_generatior(list_brackets, position, n,
                        open, close):
    if(close == n):
        for i in list_brackets:
            print(i, end='')
        print()
        return
    else:
        if(open < n):
            list_brackets[position] = '('
            brackets_generatior(list_brackets, position + 1, n,
                                open + 1, close)
        if(open > close):
            list_brackets[position] = ')'
            brackets_generatior(list_brackets, position + 1, n,
                                open, close + 1)


if __name__ == '__main__':
    n = int(input())
    list_brackets = [''] * 2 * n
    brackets(list_brackets, n)
