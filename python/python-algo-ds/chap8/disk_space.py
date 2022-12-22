"""
Computing the size of a directory is a postorder traversal
    since we need to calculate the size of all the children
    before the size of a directory can be calculated
"""


def disk_space(T, p):
    subtotal = (
        p.element().space()
    )  # assuming element has a space method that returns the space
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal
