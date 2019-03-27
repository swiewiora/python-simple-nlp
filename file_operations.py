def read_file():
    text = ''

    with open('input.txt') as file:
        lines = file.readlines()
        str_word_length = next(iter(lines or []), None)
        word_length = int(str_word_length)  # todo try/catch

        while True:
            sentence = next(iter(lines or []), None)
            if sentence is None:
                break
            if text == '':
                text += sentence
            else:
                text += ' ' + sentence

    return {word_length, text}
