import { expect, test } from "bun:test";
import { isValid } from "./02-isValid";

test('isValid1', () => {
  expect(isValid('()[]{}')).toBeTrue();
  expect(isValid('(})')).toBeFalse();
})

