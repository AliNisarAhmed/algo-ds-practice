import { expect, test} from 'bun:test';
import { maxProfit } from './04-maxProfit';


test("maxProfit", () => {
  expect(maxProfit([7,1,5,3,6,4])).toBe(5);
})
