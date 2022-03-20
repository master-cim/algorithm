# I. Любители конференций
# ID успешной посылки 66248195
from collections import Counter


def conference_lovers(id_university, k):
    number_participant = Counter(id_university)
    k_max = number_participant.most_common()[0:k:]
    result = [univer[0] for univer in k_max]
    print(' '.join(map(str, result)))


def read_input():
    _ = int(input())
    id_university = [int(element) for element in input().strip().split()]
    k = int(input())
    return(id_university, k)


if __name__ == '__main__':
    id_university, k = read_input()
    conference_lovers(id_university, k)
