package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.StdOut;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;

// 1.2.11
// 1.2.12
public class SmartDate {
  private final int month;
  private final int day;
  private final int year;

  public SmartDate(int y, int m, int d) {
    if (!isValidDate(y, m, d)) {
      throw new RuntimeException("Invalid Date");
    }

    year = y;
    month = m;
    day = d;
  }

  public SmartDate(String date) {
    String[] fields = date.split("/");
    year = Integer.parseInt(fields[0]);
    month = Integer.parseInt(fields[1]);
    day = Integer.parseInt(fields[2]);

    if (!isValidDate(year, month, day)) {
      throw new RuntimeException("Invalid Date in String");
    }
  }

  private boolean isValidDate(int year, int month, int day) {
    int[] maxDaysPerMonth = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    if (year < 1 || month < 1 || month > 12 || day < 1 ||
        day > maxDaysPerMonth[month - 1]) {
      return false;
    }

    return true;
  }

  @Override
  public String toString() {
    return year + "-" + month + "-" + day;
  }

  // Numberphile: https://www.youtube.com/watch?v=z2x3SSBVGJU
  public String dayOfTheWeek() {
    LocalDate date = LocalDate.of(year, month, day);
    DayOfWeek dow = date.getDayOfWeek();
    return dow.getDisplayName(TextStyle.FULL, Locale.getDefault());
  }

  public static void main(String[] args) {
    SmartDate sm = new SmartDate(1987, 4, 8);
    StdOut.println(sm.dayOfTheWeek());
    sm = new SmartDate(2022, 2, 27);
    StdOut.println(sm.dayOfTheWeek());
    sm = new SmartDate(1987, 3, 10);
    StdOut.println(sm.dayOfTheWeek());
  }
}
