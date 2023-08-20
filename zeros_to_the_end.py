def move_zeros(input_lst: 'list[int]') -> 'list[int]':
    reversed_list: list[int] = input_lst[::-1]  
    for index, num in enumerate(reversed_list):
        if not num:
            reversed_list.insert(0, reversed_list.pop(index))
    return reversed_list[::-1]

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
