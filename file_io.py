def read_file(file_name):
    """Reads input file. First line should contain size of array
    (ValueException), others sequence of sentences.
    :param file_name: input file name
    :type file_name: str
    :return (array length, input text)
    :rtype (int, str)
    :raise ValueError
    """
    text = ''

    with open(file_name) as file:
        lines = file.readlines()
        iterator_lines = iter(lines or [])
        str_word_length = next(iterator_lines, None)
        try:
            w = int(str_word_length)
        except ValueError:
            print('Word length is not an integer')
            raise

        while True:
            sentence = next(iterator_lines, None)
            if sentence is None:
                break
            if text == '':
                text = sentence
            else:
                text += ' ' + sentence

    return w, text


def write_file(array_list, file_name):
    """"Write converted array list into output file.
    :param array_list: list of character arrays
    :type array_list: list of str
    :param file_name: output file name
    :type file_name: str
    """
    with open(file_name, 'w') as file:
        file.writelines('\n'.join(array_list))
