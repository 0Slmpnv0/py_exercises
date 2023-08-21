#https://www.codewars.com/kata/541c8630095125aba6000c00


def digital_root(n: int, result:int=0) -> int:
    if not n:
        if result > 9:
            return digital_root(result)
        return result

    return digital_root(n // 10, result + n % 10)
