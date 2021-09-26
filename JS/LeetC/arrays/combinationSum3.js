function combinationSum3(k, n) {
  let res = [];
  let comb = [];
  backtrack(n, comb, 0);
  return res;

  function backtrack(remain, comb, start) {
    if (remain < 0) {
      return;
    }

    if (remain === 0 && comb.length === k) {
      res.push([...comb]);
      return;
    }

    for (let i = start; i < 9; i++) {
      comb.push(i + 1);
      backtrack(remain - i - 1, comb, i + 1);
      comb.pop();
    }

  }
}
