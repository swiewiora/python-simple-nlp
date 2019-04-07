# Python Simple NLP
The purpose of this project was to write a program which, given a 
sequence of sentences in natural language and constant w, would set the 
words into one or more character arrays of length w, so that:
- The order of words (and sentences) is kept,
- No words are split between 2 arrays,
- All arrays are filled as much as possible.
Words shall be separated by a single whitespace as well as the sentences. 
Punctuation shall be kept and treated as part of the words. 
It is assumed that no word is longer than w characters.

Example of input:

    12
    Blah blah blah.
    Hello world!
    It is I, Bob.

## Install

Create a virtual environment (Python 3 built-in venv) and (optionally) 
activate it:

    python3 -m venv venv
    . venv/bin/activate

Or on Windows cmd:

    python -m venv venv
    venv\Scripts\activate.bat

Install Simple-NLP:

    pip install .

## Run

If no parameters are given, programs runs in 'interactive' mode in which
User will be asked to input data into terminal:

    python simplenlp
    
Output will be printed to console. To input data from file, second 
parameter must be a name of an input file:

    python simplenlp input.txt
    
By default, program saves input to 'output.txt'. To rename output file,
simply put it as second parameter:

    python simplenlp some-input.txt some-output.txt

The order is important. If the output file exists, it will be overwritten.

## Debug

run main script in a debugger of your choice.
