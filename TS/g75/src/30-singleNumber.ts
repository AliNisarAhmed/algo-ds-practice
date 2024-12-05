function singleNumber(nums: number[]): number {
  let result = 0;
  for (let n of nums) {
    result = result ^ n;
  }

  return result;
}
