function addBinary(a: string, b: string): string {
  let x = BigInt(`0b${a}`);
  let y = BigInt(`0b${b}`);

  while (y) {
    let answer = x ^ y;
    let carry = (x & y) << BigInt(1);
    x = answer;
    y = carry;
  }

  return x.toString(2);
}

export default addBinary;
