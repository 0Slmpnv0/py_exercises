def prepare_piglatin_word(word:str)-> str:
    letters_list = list(word)
    piglatin_word = letters_list.append(letters_list.pop(0))
    return ''.join(piglatin_word)


def pig_it(text: str):
    words_list: 'list[str]' = text.split()
    words_list = list(map(prepare_piglatin_word(words_list)))
    print(words_list)


pig_it('hui hui hui')
