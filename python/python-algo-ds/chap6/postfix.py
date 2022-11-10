from stack import ArrayStack


def eval_postfix(string):
    s = ArrayStack()
    for c in string:
        if isOperator(c):
            rhs = s.pop()
            lhs = s.pop()
            result = applyOperator(c, int(lhs), int(rhs))
            s.push(result)
        else:
            s.push(c)

    return s.pop()


def isOperator(c):
    return c in "+-/*"


def applyOperator(op, lhs, rhs):
    match op:
        case "+":
            return lhs + rhs
        case "/":
            return lhs / rhs
        case "-":
            return lhs - rhs
        case _:
            return lhs * rhs
