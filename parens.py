# -*- coding: utf-8 -*-
from stack import Stack


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
    s = Stack()
    balanced = True
    count = 0
    while count < len(uni_str) and balanced:
        char = uni_str[count]
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.ll.size_ == 0:
                return -1
                balanced = False
            else:
                s.pop()

        count += 1

    if balanced and s.ll.size_ == 0:
        return 0
    else:
        return 1
