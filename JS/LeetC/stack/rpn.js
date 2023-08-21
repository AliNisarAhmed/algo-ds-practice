/**
 * @param {string[]} tokens
 * @return {number}
 */
const OPERATORS = {
  "+": (a, b) => a + b,
  "-": (a, b) => a - b,
  "*": (a, b) => a * b,
  "/": (a, b) => (a / b > 0 ? Math.floor(a / b) : Math.ceil(a / b)),
};

function evalRPN(tokens) {
  const stack = [];

  for (const token of tokens) {
    if (!isOperator(token)) {
      stack.push(Number(token));
      continue;
    }

    let b = stack.pop();
    let a = stack.pop();
    let result = OPERATORS[token](a, b);
    stack.push(result);
  }

  return stack.pop();
}

function isOperator(token) {
  return Object.keys(OPERATORS).includes(token);
}

(() => {
  let arr = [
    "10",
    "6",
    "9",
    "3",
    "+",
    "-11",
    "*",
    "/",
    "*",
    "17",
    "+",
    "5",
    "+",
  ];
  console.log(evalRPN(arr));
})();
