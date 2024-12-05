function twoSum(nums, target) {
  const obj = {};
  for (let [index, num] of nums.entries()) {
    if (obj[target - num] !== undefined) {
      return [index, obj[target - num]];
    } else {
      obj[num] = index;
    }
  }
}
