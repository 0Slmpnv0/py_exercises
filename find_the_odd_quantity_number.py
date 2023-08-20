from collections import Counter


def find_it(seq: 'list[int]'):
    for number, quantity in Counter(seq).items():
        if quantity % 2:
            return number


print(find_it(seq=[1, 2, 2]))
