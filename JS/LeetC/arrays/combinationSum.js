function combinationSum(candidates, target) {
  const res = [];
  const comb = [];

  backtrack(target, comb, 0, candidates, res);
  return res;

  function backtrack(remain, comb, start) {
    if (remain === 0) {
      res.push([...comb]);
      return;
    }

    if (remain < 0) {
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      comb.push(candidates[i]);
      backtrack(remain - candidates[i], comb, i);
      comb.pop();
    }
  }
}

console.log(combinationSum([2, 3, 5], 8))
