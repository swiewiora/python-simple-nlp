def read_file():
    with open('input.txt') as file:
        lines = file.readlines()
        str_word_length = next(iter(lines or []), None)
        int(str_word_length)  # todo try/catch

        text = ''
        while True:
            sentence = next(iter(lines or []), None)
            if sentence is None:
                break
            if text == '':
                text += sentence
            else:
                text += ' ' + sentence
        return text
