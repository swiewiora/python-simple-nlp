def get_length():
    """Takes length of character array from input. If not a number,
    throws ValueException.
    :return length of character array
    :rtype int
    :raise ValueException
    """
    str_w = input('Input length of a single word: ')
    try:
        return int(str_w.strip())
    except ValueError:
        print('Word length must be an integer')
        raise


def get_input_string():
    """""Reads string of words separated by space from user input
    :return string of words separated by space
    :rtype str
    """
    print('Insert sentences in new lines. To stop insertion, enter empty line')
    text = ''
    while True:
        sentence = input()
        if sentence == '':
            break
        if text == '':
            text = sentence
        else:
            text += ' ' + sentence
    return text


def print_array_list(array_list):
    """"Output converted array list to console
    :param array_list: list of character arrays
    :type array_list: list of str
    """
    print(*array_list, sep="\n")
