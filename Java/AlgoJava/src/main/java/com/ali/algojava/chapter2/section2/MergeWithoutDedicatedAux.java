package com.ali.algojava.chapter2.section2;

public class MergeWithoutDedicatedAux {

  public static void sort(Comparable[] a) {
    Comparable[] aux = new Comparable[a.length];

    sort(a, aux, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi) {
    if (hi <= lo) {
      return;
    }

    int mid = lo + (hi - lo) / 2;
    sort(a, aux, lo, mid);
    sort(a, aux, mid + 1, hi);

    merge(a, aux, lo, mid, hi);
  }

  private static void merge(Comparable[] array, Comparable[] aux, int lo, int mid, int hi) {
    for (int i = lo; i <= hi; i++) {
      aux[i] = array[i];
    }

    int indexLeft = lo;
    int indexRight = hi;
    int arrayIndex = lo;

    while (indexLeft <= mid && indexRight <= hi) {
      if (aux[indexLeft].compareTo(aux[indexRight]) <= 0) {
        array[arrayIndex] = aux[indexLeft];
        indexLeft++;
      } else {
        array[arrayIndex] = aux[indexRight];
        indexRight++;
      }
      arrayIndex++;
    }

    while (indexLeft <= mid) {
      array[arrayIndex] = aux[indexLeft];
      indexLeft++;
      arrayIndex++;
    }
  }

}
