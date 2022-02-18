def to_binary(number: int) -> str:
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number = number // 2
    return(b)

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
