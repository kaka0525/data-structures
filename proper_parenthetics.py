from __future__ import unicode_literals


def proper_parenthetics(input):
    # Keep track of how many open parens ("(") we find
    open_parens = 0
    for c in input:
        if c == '(':
            open_parens += 1
        elif c == ')':
            open_parens -= 1
        if open_parens < 0:
            # If it ever drops below 0, we know there's some ")" that is
            # not paired, so it's broken.
            return -1
    if open_parens > 0:
        # Some "(" is left unpaired, so it's open.
        return 1
    else:
        # Then it must be balanced!
        return 0


print proper_parenthetics(')))))')
