function radixSort(numArr) {
  const maxDigits = mostDigits(numArr);

  for (let k = 0; k < maxDigits; k++) {
    let bucket = Array.from({ length: 10 }, () => []);

    for (let i = 0; i < numArr.length; i++) {
      let kthDigit = getDigit(numArr[i], k);

      bucket[kthDigit].push(numArr[i]);
    }
    numArr = [].concat(...bucket);
  }

  return numArr;
}

console.log(radixSort([1234, 123, 12, 1, 345, 3456, 34567]))


// Helpers

function getDigit(num, place) {
  // place starts from right, with rightmost value a place of 0
  return Math.floor(Math.abs(num) / (Math.pow(10, place))) % 10;
}

function digitCount(num) {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

function mostDigits(numArr) {
  return Math.max(...numArr.map(digitCount));
}

// getDigit(7654, 2);
// 7654 / 10^2
// = 76.54
// = 76
// = 76 % 10
// = 6

// digitCount(7654)
// log10 7654 => 10^x = 7654 = 10^3 + something in decimals