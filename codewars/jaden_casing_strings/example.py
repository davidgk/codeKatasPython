from functools import reduce

def make_upper_case(acum,  value):
    capitalized = value.capitalize()
    return capitalized if acum == "" else acum + " " + capitalized

def solution(a):
    initial = str(a).strip()
    return "" if len(initial) == 0 else reduce(make_upper_case, initial.split(" "), "")


# Another interesting approach from codewars

def to_jaden_case_01(string):
    return ' '.join(map(str.capitalize, string.split()))

def to_jaden_case_02(string):
    return ' '.join(word.capitalize() for word in string.split())