# G. Гардероб
# ID успешной посылк 66169913

def fast_sort_items(color_items):
    less = []
    equal = []
    greater = []
    for color in color_items:
        if color == '0':
            less.append(color)
        elif color == '1':
            equal.append(color)
        else:
            greater.append(color)
    print(*(less + equal + greater))


def read_input():
    _ = int(input())
    color_items = (input().split())
    return color_items


if __name__ == '__main__':
    color_items = read_input()
    fast_sort_items(color_items)
