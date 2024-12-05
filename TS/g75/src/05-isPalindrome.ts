function isPalindrome(s: string): boolean {
  let i = 0;
  let j = s.length - 1;

  while (i < j) {
    if (!isAlpha(s[i])) {
      i++;
    } else if (!isAlpha(s[j])) {
      j--;
    } else {
      if (s[i].toLowerCase() !== s[j].toLowerCase()) {
        return false;
      }

      i++;
      j--;
    }
  }

  return true;
}

function isAlpha(s: string) {
  return /[a-zA-Z0-9]/g.test(s[0]);
}
