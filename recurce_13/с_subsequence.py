# C. Подпоследовательность
# ID успешной посылки 66120090

def subsequence(sub_line, whole_line):
    position = -1
    for i in sub_line:
        position = whole_line.find(i, position + 1)
        if position == - 1:
            return False
    return True


def read_input():
    sub_line = input()
    whole_line = input()
    return sub_line, whole_line


if __name__ == '__main__':
    sub_line, whole_line = read_input()
    print(subsequence(sub_line, whole_line))
