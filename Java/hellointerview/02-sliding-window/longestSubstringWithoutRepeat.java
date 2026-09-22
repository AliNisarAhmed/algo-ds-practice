import java.util;

public class Solution {
  public Integer longestSubstringWithoutRepeat(String s) {
    // state
    var seen = new HashMap<>();
    int result = 0;
    var start = 0;

    for (int end = 0; end < s.length(); end++) {
      char ch = s.charAt(end);
      seen.put(ch, seen.getOrDefault(ch, 0) + 1);
      while (seen.get(ch) > 1) {
        char startChar = s.charAt(start);
        seen.put(startChar, seen.get(startChar) - 1);
        start++;
      }
      result = Math.max(result, end - start + 1);
    }
    return result;
  }
}
