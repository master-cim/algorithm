from re import I
from unittest import result


def is_palindrome(line: str) -> bool:
    rem_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ',
                '!', '"', '#', '$', '%', '&', '\', ''',
                '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_',
                '`', '{', '|', '}', '~', '\t', '\n', '\r', '\x0b', '\x0c']
    clean = (''.join([line[i] for i in range(
        len(line)) if line[i] not in rem_list])
             ).lower()
    if len(clean) == 1:
        return 'True'
    left = 0
    right = len(clean)-1
    while left < right:
        if clean[left] != clean[right]:
            result = 'False'
        else:
            result = 'True'
            left += 1
            right -= 1
        return result


print(is_palindrome(input().strip()))