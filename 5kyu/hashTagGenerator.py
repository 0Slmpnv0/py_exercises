#https://www.codewars.com/kata/52449b062fb80683ec000024


input_string = input()

words_list = [element.capitalize() for element in input_string.split(' ')]

hashtag = '#' + ''.join(words_list)

if len(hashtag) > 140 or not input_string:
    print('false')
    exit()

print(hashtag)
