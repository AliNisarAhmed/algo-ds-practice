function solution(isBadVersion: (number) => boolean) {
  return (n: number) => helper(0, n);

  function helper(start: number, end: number) {
    while (start < end) {
      let mid = Math.floor(start + (end - start) / 2);

      if (!isBadVersion(mid)) {
        start = mid + 1;
      } else { 
        end = mid;
      }
    }

    return start;
  }
}
