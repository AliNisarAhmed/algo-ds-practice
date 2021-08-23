function countOnes(n) {
  let count = 0; 

  while (n) {
    n = n & (n - 1);
    count++;
  }

  return count;
}

console.log(countOnes(4));
