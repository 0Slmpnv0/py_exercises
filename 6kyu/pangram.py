#https://www.codewars.com/kata/545cedaa9943f7fe7b000048


import string


def is_pangram(input_string:str) -> bool:
    alphabet = set(string.ascii_lowercase)
    input_pangram_set = set((input_string.lower()))
    return input_pangram_set >= alphabet