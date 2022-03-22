# E. Покупка домов
# ID успешной посылки 66298098

def potential_shopping(price_house, cash):
    sum_houses = 0
    item = 0
    if len(price_house) == 1:
        return 1
    elif len(price_house) != 0:
        while sum_houses <= cash:
            sum_houses += price_house[item]
            item += 1
        return item - 1
    else:
        return 0


def read_input():
    input_list = list(map(int, input().split()))
    cash = input_list[1]
    price_house = list(map(int, input().split()))
    price_house = sorted([item for item in price_house if item <= cash])
    return cash, price_house


if __name__ == '__main__':
    cash, price_house = read_input()
    print(potential_shopping(price_house, cash))
