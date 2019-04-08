import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='simplenlp',
    version='1.0',
    zip_safe=False,
    packages=setuptools.find_packages(),
    author='Sebastian Wiewiora',
    author_email='sebawiewior@gmail.com',
    description='Python program which converts sequence of sentences in '
                'natural language and constant w into one or more '
                'character arrays of length w',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swiewiora/python-simple-nlp',
    license='MIT',
 )
