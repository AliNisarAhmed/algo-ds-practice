import { expect, test } from "bun:test";
import addBinary from "./19-addBinary";
test("addBinary", () => {
  expect(addBinary("11", "1")).toBe("100");
});
