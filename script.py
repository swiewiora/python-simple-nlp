import numbers

def get_length():
    word_length = input('Input length of a single word')

    if (isinstance(word_length, numbers.Integral) ):
        return word_length
    else:
        raise Exception ('Number is not integer')


def get_input_string():
    text = input('Input text')
    words = text.split()

    # return input_text

# def parse_input (string):
