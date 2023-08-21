#https://www.codewars.com/kata/566d5e2e57d8fae53c00000c


import random

def get_bingo_card():
    step = 15
    result:list[str] = []
    lowest = 1
    number_quantity = 5
    useless_N = 10
    for letter in 'BINGO':
        rand_nums: list[int] = random.sample(range(lowest, lowest + step), number_quantity)
        result += [f'{letter}{num}' for num in rand_nums]
        lowest += step
        
    result.pop(useless_N) 
    return result