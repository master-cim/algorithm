# H. Большое число
# ID успешной посылки 66119080


def big_number(digits, arr):
    for i in range(digits - 1):
        for j in range(0, digits-i-1):
            var1 = arr[j] + arr[j+1]
            var2 = arr[j + 1] + arr[j]
            if var1 < var2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(''.join(arr))


def read_input():
    digits = int(input())
    arr = input().split(' ')
    return digits, arr


if __name__ == '__main__':
    digits, arr = read_input()
    print(big_number(digits, arr))
