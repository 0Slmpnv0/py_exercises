#https://www.codewars.com/kata/514b92a657cdc65150000006/

def solution(number: int):
    total_sum = 0
    for num in range(1, number):
        if not num % 3 or not num % 5:
            total_sum += num
    return total_sum