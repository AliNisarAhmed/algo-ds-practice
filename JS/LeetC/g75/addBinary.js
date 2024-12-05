// a and b are string representation of binary
function addBinary(a, b) {
  let x = parseInt(a, 2);
  let y = parseInt(b, 2);
  while (y !== 0) {
    x = x ^ y;
    y = (x & 1) << 1;
  }

  return x.toString(2);
}
