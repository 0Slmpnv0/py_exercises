#https://www.codewars.com/kata/54da5a58ea159efa38000836


from collections import Counter


def find_it(seq: 'list[int]'):
    for number, quantity in Counter(seq).items():
        if quantity % 2:
            return number


print(find_it(seq=[1, 2, 2]))
