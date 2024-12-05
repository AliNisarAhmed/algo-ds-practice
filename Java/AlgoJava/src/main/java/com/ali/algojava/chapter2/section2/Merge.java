package com.ali.algojava.chapter2.section2;

public class Merge {
  private static Comparable[] aux;

  public static void sort(Comparable[] a) {
    aux = new Comparable[a.length]; // allocate space only once
    sort(a, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo)
      return;
    int mid = lo + (hi - lo) / 2;
    sort(a, lo, mid);
    sort(a, mid + 1, hi);
    merge(a, lo, mid, hi);
  }

  public static void merge(Comparable[] a, int lo, int mid, int hi) {
    int i = lo;
    int j = mid + 1;

    for (int k = lo; k <= hi; k++) { // copy a[lo..hi] to aux[lo..hi]
      aux[k] = a[k];
    }

    for (int k = lo; k <= hi; k++) {
      if (i > mid) {
        a[k] = aux[j++]; // just copy right side
      } else if (j > hi) {
        a[k] = aux[i++]; // just copy left side
      } else if (less(aux[j], aux[i])) {
        a[k] = aux[j++];
      } else {
        a[k] = aux[i++];
      }
    }
  }

  private static boolean less(Comparable v, Comparable w) {
    return v.compareTo(w) < 0;
  }
}


// 2.2.1
// A E Q S U Y E I N O S T
// __ || __ || A E Q S U Y :: E I N O S T
// 0  || A  || E Q S U Y :: E I N O S T
// 1  || A E || Q S U Y :: E I N O S T
// 2  || A E E || Q S U Y :: I N O S T 
// 3  || A E E I || Q S U Y :: N O S T
// 4  || A E E I N || Q S U Y :: O S T
// 5  || A E E I N O || Q S U Y :: S T 
// 6  || A E E I N O Q || S U Y :: S T 
// 7  || A E E I N O Q S || U Y :: S T 
// 8  || A E E I N O Q S S || U Y :: T 
// 9  || A E E I N O Q S S T || U Y ::
// 10 || A E E I N O Q S S T U Y


// 2.2.2
// E A S Y Q U E S T I O N
// A E 
//     S Y
// A E S Y
//         Q U
//             E S 
//         E Q S U
// A E E Q S S U Y
//                 I T 
//                     N O
//                 I N O T
// A E E I N O Q S S T U Y

// 2.2.3
// Same as above but Bottom-up
// E A S Y Q U E S T I O N
// A E 
//     S Y
//         Q U
//             E S 
//                 I T
//                     N O
// A E S Y
//         E Q S U
//                 I N O T
// A E E Q S S U Y
// A E E I N O Q S S T U Y

// 2.2.4
// Yes, the merge algo requires the sub arrays to be sorted

// 2.2.5
// Bottom up
// 2 x19 times
// 4 x9 times and 3 x1 times (leftover)
// 8 x4 times and 7 x1 times (leftover)
// 16, 16
// 32
// 39 (32 from above plus 7 leftovers)
