#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def line_to_right(input_list: "list[list[int]]") -> 'list[int]':
    return input_list.pop(0)


def line_down(input_list: "list[list[int]]") -> 'list[int]':
    return_list: list[int] = []
    for underlist in input_list:
        return_list += [underlist.pop(-1)]
    return return_list


def line_to_left(input_list: "list[list[int]]") -> 'list[int]':
    return input_list.pop(-1)[::-1]


def line_up(input_list: "list[list[int]]") -> 'list[int]':
    return_list: list[int] = []
    for underlist in input_list:
        return_list += [underlist.pop(0)]
    return return_list[::-1]


def snail(input_list:'list[list[int]]'):
    return_list: list[int]= []
    while input_list:
        for number in line_to_right(input_list):
            return_list.append(number)
        for number in line_down(input_list):
            return_list.append(number)
        if input_list:
            for number in line_to_left(input_list):
                return_list.append(number)
            for number in line_up(input_list):
                return_list.append(number)
    return return_list

