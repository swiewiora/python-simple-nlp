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
