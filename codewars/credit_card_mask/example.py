def maskify(cc):
    if len((str(cc) or "").strip()) < 5:
        return cc
    else:
        to_replace = str(cc)[4:]
        replaced = ""
        for _ in to_replace:
            replaced = replaced + "#"
        return replaced + cc[(len(cc) - 4):]

# Other approach:

# return masked string
def maskify2(cc):
    return "#"*(len(cc)-4) + cc[-4:]


def maskify3(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]