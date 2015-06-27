# -*- coding: utf-8 -*-


def paren_check(uni_str):
    """
    Verify unicode string input for proper use of opening and closing
    parenthesis within given code.
        arg:
            uni_str: Unicode string value (does not validate)

        return:
            1: Return value of 1 if opening parenthesis provided,
                and not closed.
            0: Return value of 0 if all opening and closing parenthesis are
                complete.
            -1: Return -1 value if closing parenthesis is provided without
                first providing opening parenthesis.
    """
    count = 0
    for char in uni_str:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count == -1:
            return count
    if count > 0:
        return 1
    return count
