import java.util.Arrays;

public class Solution {
  public int maxScore(int[] cards, int k) {
    int total = Arrays.stream(cards).sum();

    if (k >= cards.length) {
      return total;
    }

    int windowSum = 0;
    int result = 0;
    int start = 0;

    for (int end = 0; end < cards.length; end++) {
      windowSum += cards[end];
      if (end - start + 1 == cards.length - k) {
        result = Math.max(result, windowSum);
        windowSum -= cards[start];
        start++;
      }
    }

    return result;
  }
}
