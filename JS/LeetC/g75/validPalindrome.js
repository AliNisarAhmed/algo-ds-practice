function isPalindrome(str) {
  let i = 0;
  let j = str.length - 1;

  while (i < j) {
    const left = str[i];
    const right = str[j];

    if (!isAlpha(left)) {
      i++;
    } else if (!isAlpha(right)) {
      j--;
    } else {
      if (left.toLowerCase() !== right.toLowerCase) {
        return false;
      }
      i++;
      j--;
    }
  }

  return true;
}

function isAlpha(s) {
  return /[a-zA-Z0-9]/.test(s[0]);
}
