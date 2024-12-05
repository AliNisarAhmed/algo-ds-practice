export function isValid(s: string): boolean {
  const stack: string[] = [];

  for (let b of s) {
    if (isOpeningBracket(b)) {
      stack.push(b);
    } else if (isClosingBracket(b)) {
      const last = stack.pop();

      if (!last) {
        return false;
      }

      if (!bracketsMatch(last, b)) {
        return false;
      }
    }
  }

  return stack.length === 0;
}

function bracketsMatch(op: string, cl: string): boolean {
  switch (op) {
    case "{":
      return cl === "}";
    case "(":
      return cl === ")";
    case "[":
      return cl === "]";
    default:
      return false;
  }
}

function isOpeningBracket(s: string): boolean {
  return "({[".includes(s);
}

function isClosingBracket(s: string): boolean {
  return ")}]".includes(s);
}
