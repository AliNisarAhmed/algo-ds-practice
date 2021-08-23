function isPowerOfFour(n) {
  return !(n & (n - 1)) && (n & 0x55555555);
}

console.log(isPowerOfFour(4^2))
