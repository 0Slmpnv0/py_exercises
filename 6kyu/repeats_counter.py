#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


from collections import defaultdict
from typing import DefaultDict

input_str = input().lower()

char_counter: DefaultDict[str, int] = defaultdict(int)

for char in input_str:
    char_counter[char] += 1

repeats_counter: 'dict[str, int]' = {key: val for key, val in char_counter.items() if val > 1}

print(len(repeats_counter))
