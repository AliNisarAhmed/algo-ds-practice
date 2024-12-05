function solution(isBadVersion) {
  return n => helper(0, n);

  function helper(start, end) {
    if (start === end) {
      return start;
    }

    if (start - end === 1) {
      return start;
    }

    let mid = Math.floor(start + (end - start) / 2);
    if (isBadVersion(mid)) {
      return helper(start, mid);
    } else {
      return helper(mid + 1, end)
    }
  }
}
