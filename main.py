import script

w = script.get_length()
input_text = script.get_input_string()
array_list = script.to_char_arrays(input_text, w)
script.print_array_list(array_list)
