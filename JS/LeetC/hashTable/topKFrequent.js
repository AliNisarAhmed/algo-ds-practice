function topKFrequent(nums, k) {
  let counts = {};

  for (let e of nums) {
    counts[e] = counts[e] === undefined ? 1 : counts[e] + 1;
  }

  let res = Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .map((x) => x[0]);
  res.length = k;
  return res;
}
