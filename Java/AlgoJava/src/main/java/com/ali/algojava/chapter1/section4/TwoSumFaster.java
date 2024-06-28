package com.ali.algojava.chapter1.section4;

import java.util.HashMap;
import java.util.Map;

public class TwoSumFaster {

  public static int twoSumFaster(int[] arr) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int key : arr) {
      int freq = map.getOrDefault(key, 0);
      map.put(key, freq + 1);
    }

    int count = 0;

    for (int key : arr) {
      if (map.containsKey(-key)) {
        count += map.get(-key);
      }

      if (key == 0) {
        count--;
      }
    }
    return count / 2;
  }
}
