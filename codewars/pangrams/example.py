from functools import reduce


def filter_data(acum,  value):
    if value.isalpha():
        if value in acum:
            acum[value] = acum[value] + 1
        else:
            acum[value] = 1
    return acum
    # try:
    #     pass
    # except Exception as ex:
    #     print(ex)
    #     return acum

def solution(aPhrase):
    initial = list(str(aPhrase).strip().lower())
    if len(initial) == 0:
        return False
    else:
        return len(reduce(filter_data, initial, {})) == 26

# otjher interesting solutions

import string

def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True


def is_pangram2(s):
    return set(string.ascii_lowercase).issubset(s.lower())

def is_pangram3(input_string):
    """Returns False if the input string is not a pangram else returns True"""
    return False if [char for char in string.ascii_lowercase if not char in input_string.lower()] else True