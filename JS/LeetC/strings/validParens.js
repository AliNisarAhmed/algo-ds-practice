function isValid(s) {
  if (s.length === 0) return true;
  if (s.length % 2 === 1) return false;
  let stack = [];

  let starters = {
    "{": "}",
    "[": "]",
    "(": ")",
  };

  for (let i = 0; i < s.length; i++) {
    let current = s[i];

    if (starters[current]) {
      stack.push(current);
    } else {
      let lastBracket = stack.pop();
      if (!lastBracket) return false;

      if (starters[lastBracket] !== current) return false;
    }
  }

  return stack.length === 0;
}
