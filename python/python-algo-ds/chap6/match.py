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

        tag, *rest = raw[j + 1: k].split()

        if not tag.startswith('/'):
            S.push(tag)

        else:
            if S.is_empty():
                return False

            if tag[1:] != S.pop():
                return False

        j = raw.find('<', k + 1)

    return S.is_empty()


# https://stackoverflow.com/questions/72936806/non-recursive-algorithm-for-all-permutations-using-a-stack
def perm_rec(items):
    _perm_rec([], list(items))


def _perm_rec(perm, items):
    if len(items) == 0:
        print(perm)
    else:
        for i in range(len(items)):
            perm.append(items.pop(0))
            _perm_rec(perm, items)
            items.append(perm.pop())


def perm_explicit_stack(items):
    items = list(items)
    n = len(items)
    s = ArrayStack()
    i = 0
    perm = []

    while i < n:
        perm.append(items.pop(0))
        s.push(i)
        i = 0

        if len(items) == 0:
            print(perm)

            while i == len(items) and s:
                i = s.pop()
                items.append(perm.pop())
                i += 1
