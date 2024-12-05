function hammingWeight(n: number): number {
  let count = 0;
  while (n !== 0) {
    count++;
    n = n & n - 1; 
    // AND of n and n - 1 converts the last 1 in n to 0
    // thus above code just checks how many time we can keep ANDing n and n - 1
  }
}
