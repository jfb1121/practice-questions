"""
write a function to revers the words of a string in the form of a char[] 
in place.
No additional lists / arrays can be used.
No internal library functions to be used.

have included a way to do the same thing using splicing. 
"""


# input: ['I', ' ', 'L', 'O', 'v', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g', 's']
# output: ['I', ' ', 'e', 'v', 'o', 'l', ' ', 's', 'g', 'n', 'i', 'r', 't', 's']


def reverse_char_arr_in_place(string):
    """
    function to reverse a string in the form of a char array in place.
    """
    i = 0
    j = 0
    str_len = len(string)

    while i < str_len:
        while j < str_len and string[j] != ' ':
            j = j + 1

        # j - 1 because we want to send end of the word
        # and the inner while loop traverses until string[j] becomes == ' '
        revers_word_using_splicing(string, i, j)

        i = j+1
        j = i

    return string


def reverse_word(string,
                 word_start,
                 word_end):
    """
    reverses a sub string from start index to end index in place. 
    """
    # this whole function could be replaced by splicing
    # see the function below

    start = word_start
    end = word_end

    if end - start > 1:
        while start >= word_start and end <= word_end and start < end:
            string[start], string[end] = string[end], string[start]

            start += 1
            end -= 1

    return string


def revers_word_using_splicing(string,
                               word_start,
                               word_end):
    """
    reverse using splicing
    """

    string[word_start:word_end] = string[word_end-1:word_start-1: -1]
