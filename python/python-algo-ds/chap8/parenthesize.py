def parenthesize(T, p):
    """
    Produces a parenthetic string representation of a tree
    e.g: 1 (2, 3, (4, 5, 6))

    essentially a preorder traversal, but we need to print '(' and ')' at the right time
    hence we cannot use the generic function
    """
    print(p.element(), end="")  # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = " (" if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthesize(T, c)
        print(")", end="")
