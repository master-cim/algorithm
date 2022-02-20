def data_input():
    k = int(input()) * 2
    matrix = ''
    matrix = ''.join([matrix + input() for i in range(4)])
    return k, matrix
def calculations():
    k, matrix = data_input()
    numbers = []
    scores = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)
 
    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= k:
            scores += 1
    print(scores)
if __name__ == '__main__':
    calculations()