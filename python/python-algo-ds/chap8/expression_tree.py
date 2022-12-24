from linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """
    An arithmetic expression tree
    """

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree

        In a single parameter form, token should be a leaf value (e.g. '42'),
        and the expression tree will have that value at an isolated node

        in a three-parameter version, token should be an operator,
        and left and right should be existing ExpressTree instances that
        become the operands for the binary operator
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")

        self._add_root(token)  # use inherited non public method

        if left is not None:  # presumably three parameter form
            if token not in "+-*x/":
                raise ValueError("token must be a valid operator +-*x/")
            self._attach(self.root(), left, right)  # use inherited, non public method

    def __str__(self):
        pieces = []  # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtee to resulting list"""

        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    def evaluate(self):
        return self._evalute_recur(self.root())

    def _evalute_recur(self, p):
        """Return numeric result of subtree stored at p"""

        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evalute_recur(self.left(p))
            right_val = self._evalute_recur(self.right(p))
            match op:
                case "+":
                    return left_val + right_val
                case "-":
                    return left_val - right_val
                case "/":
                    return left_val / right_val
                case _:
                    return left_val * right_val


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon a tokenized expression"""

    S = []  # using python list as stack

    for t in tokens:
        if t in "+-x*/":
            S.append(t)  # push the operator symbol
        elif t not in "()":
            S.append(ExpressionTree(t))
        elif t == ")":
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
        # we ignore a left parenthesis

    return S.pop()


if __name__ == "__main__":
    tokens = "(((3+1)x4)/((9-5)+2))"
    tree = build_expression_tree(tokens)
    print(f"{str(tree)} = {tree.evaluate()}")
