# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

alphabet = string.ascii_letters


def make_rangoli(n):
    letters = alphabet[0:n]
    line_sub_lists = make_line_sub_lists(letters)
    line_content = [make_middle_line(x) for x in line_sub_lists]
    w = len(line_content[-1])
    upper_lines = make_upper_lines(line_content, w)
    lower_lines = make_upper_lines(line_content, w)
    top = '\n'.join(upper_lines)
    bottom = '\n'.join(lower_lines)
    return top + '\n' + bottom


def make_upper_lines(line_content, w):
    upper_lines = [
        '{message:{fill}{align}{width}}'.format(message=l, fill='-', align='^', width=w)
        for l in line_content
    ]
    return upper_lines


def make_lower_lines(line_content, w):
    lower_lines = [
        '{message:{fill}{align}{width}}'.format(message=l, fill='-', align='^', width=w)
        for l in line_content[-2::-1]
    ]
    return lower_lines


def make_line_sub_lists(letter_range):
    line_sub_lists = [letter_range[::-1][0:n+1][::-1] for n in range(0, len(letter_range))]
    return line_sub_lists


def make_middle_line(letters):
    line_end = letters[0] + ''.join(
        [
            f'-{e}' for e in letters[1::1]
        ]
    )
    return line_end[-1:0:-1] + line_end
