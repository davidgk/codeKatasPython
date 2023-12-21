from example import add_values


def test_string():
    a = 'pepe'
    b = a.upper()
    print(type(a))
    assert a == 'pepe'
    assert b == 'PEPE'
    b = b.lower()
    assert b == a
    assert a.count('p') == 2
    assert len(a) == 4
    c = '   aca   '
    assert c.strip() == 'aca'
    assert c == '   aca   '
    assert c.lstrip() == 'aca   '
    assert b.__eq__(a)
