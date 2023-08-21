#https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence: str):
    result: list[str] = []
    words_list: list[str] = sentence.split(' ')
    for word in words_list:
        if len(word) >= 5:
            word = word[::-1]
        result.append(word)
    return ' '.join(result)
