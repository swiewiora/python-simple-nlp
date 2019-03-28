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


def print_array_list(array_list):
    print(*array_list, sep="\n")
