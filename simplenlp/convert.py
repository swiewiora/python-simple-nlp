def to_char_arrays(text, w):
    """sets the words from input string into one or more character
    arrays of length w
    :param text: input string
    :param w: maximum length of array
    :type text: str
    :type w: int
    :return list of character arrays
    :rtype list of str
    """
    words = text.split()
    array_list = []
    if words:
        char_arr = words[0]  # assign first word
    else:
        char_arr = ''
    for word in words[1:]:  # for remaining words
        temp = ' ' + word
        if len(char_arr + temp) <= w:  # if second word fits
            char_arr += temp
        else:  # add  to new array
            array_list.append(char_arr)
            char_arr = word

    array_list.append(char_arr)
    return array_list
