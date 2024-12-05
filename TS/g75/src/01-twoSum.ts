export function twoSum(nums: number[], target: number): number[] {
  const obj: Record<number, number> = {};

  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    const compliment = Math.abs(current - target);
    if (obj[compliment] >= 0) {
      return [i, obj[compliment]];
    } else {
      obj[current] = i;
    }
  }

  return [];
}
