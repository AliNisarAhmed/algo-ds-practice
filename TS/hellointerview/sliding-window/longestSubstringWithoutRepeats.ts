class Solution {
  longestSubstringWithoutRepeat(s: string): number {
    let seen: { [key: string]: number } = {};
    let maxLength = 0;
    let start = 0;

    for (let end = 0; end < s.length; end++) {
      seen[s[end]] = (seen[s[end]] || 0) + 1;

      while (seen[s[end]] > 1) {
        seen[s[start]]--;
        start++;
      }

      maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;

  }

  sol2(s: string): number {
    const state = new Map<string, number>();
    let start = 0;
    let maxLength = 0;

    for (let end = 0; end < s.length; end++) {
      if (state.has(s[end])) {
        start = Math.max(start, state.get(s[end])! + 1);
      }

      state.set(s[end], end);
      maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
  }
}
