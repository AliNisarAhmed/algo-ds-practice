package com.ali.algojava.chapter1.section4;

import java.math.BigInteger;

// 1.4.2
public class ThreeSumBigInt {

  public static int count(int[] a) {
    int N = a.length;
    int count = 0;
    BigInteger bigInt;
    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        for (int k = j + 1; k < N; k++) {
          bigInt = BigInteger.valueOf(a[i]);
          bigInt = bigInt.add(BigInteger.valueOf(a[j]));
          bigInt = bigInt.add(BigInteger.valueOf(a[k]));

          if (bigInt.intValue() == 0) {
            count++;
          }
        }
      }
    }
    return count;
  }
}
