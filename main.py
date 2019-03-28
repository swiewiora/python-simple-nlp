import sys
import script
import console_io
import file_io

w = input_text = input_file_name = output_file_name = None

# todo https://stackabuse.com/command-line-arguments-in-python/
arg_count = len(sys.argv)
method = sys.argv[1]
if arg_count > 2:
    input_file_name = sys.argv[2]
if arg_count > 3:
    output_file_name = sys.argv[3]

if method == 'console':
    w = console_io.get_length()
    input_text = console_io.get_input_string()
    array_list = script.to_char_arrays(input_text, w)
    console_io.print_array_list(array_list)
elif method == 'file':
    parameters = file_io.read_file(input_file_name)
    w = parameters['word_length']
    input_text = parameters['text']
    array_list = script.to_char_arrays(input_text, w)
    file_io.write_file(array_list, output_file_name)
else:
    raise ValueError('Invalid input argument')
