"""Test for Boolean operators on constants."""

# pylint: disable=missing-docstring, invalid-name, too-many-branches, unneeded-not


def test_bool_op_on_const():
    a = 1
    b = 2
    c = 3
    if a and True:
        pass
    if a and False:
        pass
    if a or True:
        pass
    if a or False:
        pass
    if a and not 3:
        pass
    if a and 0:
        pass
    if not False:
        pass
    if not not True:
        pass
    if not not 0:
        pass
    if a or b or False:
        pass
    if a and b and False:
        pass
    while a and b and "string":
        pass
    if a or (b and (c or 0)):
        pass
    print(1 if a or 2 else 0)


def not_test_bool_op_on_const():
    a = None
    b = a or True
    if b:
        print(b or  3)
    else:
        print(b and 4)
    if (a or 0) >= 1:
        pass
