from stack import ArrayStack


def is_matched(expr):

    lefty = '({['
    righty = ')}]'

    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False

    return S.is_empty()


def is_matched_html(raw):

    S = ArrayStack()
    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j + 1)

        if k == -1:
            return False

        tag = raw[j + 1, k]

        if not tag.startswith('/'):
            S.push(tag)

        else:
            if S.is_empty():
                return False

            if tag[1:] != S.pop():
                return False

        j = raw.find('<', k + 1)

    return S.is_empty()
