import { expect, test } from "bun:test";
import { twoSum } from "./01-twoSum";

test("test 1", () => {
  const result = twoSum([2, 7, 11, 15], 9);
  expect(result.sort((a, b) => a - b)).toEqual([0, 1].sort((a, b) => a - b));
});
