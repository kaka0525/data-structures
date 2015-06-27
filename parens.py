# -*- coding: utf-8 -*-
from stack.stack import Stack


def paren_check(uni_str):
    """Write doc string"""
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

        count = count + 1

    if balanced and s.ll.size_ == 0:
        return 0
    else:
        return 1
