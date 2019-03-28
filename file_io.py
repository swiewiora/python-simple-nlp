def read_file(file_name='input.txt'):
    if file_name is None:
        file_name = 'input.txt'
    text = ''

    with open(file_name) as file:
        lines = file.readlines()
        iterator_lines = iter(lines or [])
        str_word_length = next(iterator_lines, None)
        word_length = int(str_word_length)  # todo try/catch

        while True:
            sentence = next(iterator_lines, None)
            if sentence is None:
                break
            if text == '':
                text += sentence
            else:
                text += ' ' + sentence

    dictionary = dict()
    dictionary['word_length'] = word_length
    dictionary['text'] = text
    return dictionary


def write_file(array_list, file_name='output.txt'):
    if file_name is None:
        file_name = 'output.txt'
    with open(file_name, 'w') as file:
        file.writelines("%s\n" % item for item in array_list)
