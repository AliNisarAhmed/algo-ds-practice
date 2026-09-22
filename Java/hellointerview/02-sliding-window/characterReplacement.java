import java.util.Map;

public class Solution {
  public int characterReplacement(String s, int k) {
    Map<Character, Integer> charCount = new HashMap<Character, Integer>();
    int maxFreq = 0;
    int result = 0;
    int start = 0;

    for (int end = 0; end < s.length(); end++) {
      char ch = s.charAt(end);
      charCount.put(ch, charCount.getOrDefault(ch, 0) + 1);
      maxFreq = Math.max(maxFreq, charCount.get(ch));

      while ((end - start + 1) - maxFreq > k) {
        char leftChar = s.charAt(start);
        charCount.put(leftChar, charCount.get(leftChar) - 1);
        start++;
      }

      result = Math.max(result, end - start + 1);
    }
    return result;
  }
}
