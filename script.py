def get_length():
    str_word_length = input('Input length of a single word: ')
    return int(str_word_length)  # todo try/catch


def get_input_string():
    print('Insert sentences in new lines. To stop insertion, enter empty line')
    text = ''
    while True:
        sentence = input()
        if sentence == '':
            break
        if text == '':
            text += sentence
        else:
            text += ' ' + sentence
    return text


def to_char_arrays(text, word_length):
    words = text.split()
    array_list = []
    char_arr = words[0]
    for word in words[1:]:
        temp = ' ' + word
        if len(char_arr + temp) <= word_length:
            char_arr += temp
        else:
            array_list.append(char_arr)
            char_arr = word

    array_list.append(char_arr)
    return array_list


def print_array_list(array_list):
    print(*array_list, sep="\n")
