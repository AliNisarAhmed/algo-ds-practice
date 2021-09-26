function longestPalindrome(s) {
  if (s.length === 0) return s;

  if (s.length === 1) return s;

  let left = 0;
  let right = 0;

  let res = [0, 0];

  for (let i = 0; i < s.length; i++) {
    // check if palindrome possible

    if (!checkPalindromeCondition(s, i)) {
      continue;
    }

    if (s[i] === s[i + 1]) {
      left = i;
      right = i + 1;
      while (s[left - 1] === s[left]) {
        left--;
      }

      while (s[right + 1] === s[right]) {
        right++;
      }
    } else {
      left = i - 1;
      right = i + 1;
    }

    while (s[left - 1] === s[right + 1] && left >= 0 && right < s.length - 1) {
      left--;
      right++;
    }

    if ((right - left) > (res[1] - res[0])) {
      res = [left, right];
    }
  }

  return s.slice(res[0], res[1] + 1);
}

function checkPalindromeCondition(s, i) {
  return s[i] === s[i + 1] || s[i - 1] === s[i + 1];
}

console.log(longestPalindrome('aaaa'))