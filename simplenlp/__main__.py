import sys
from simplenlp import convert, console_io, file_io


def main():
    arg_count = len(sys.argv)  # get list of arguments

    if arg_count == 1:  # console IO mode
        w = console_io.get_length()
        input_text = console_io.get_input_string()
        array_list = convert.to_char_arrays(input_text, w)
        console_io.print_array_list(array_list)

    if 1 < arg_count < 4:  # file IO mode
        input_file_name = sys.argv[1]
        if arg_count == 3:
            output_file_name = sys.argv[2]
        else:
            output_file_name = 'output.txt'  # Default file name

        w, input_text = file_io.read_file(input_file_name)
        array_list = convert.to_char_arrays(input_text, w)
        file_io.write_file(array_list, output_file_name)

    if arg_count > 3:
        raise ValueError('Invalid input argument')


if __name__ == '__main__':
    main()
