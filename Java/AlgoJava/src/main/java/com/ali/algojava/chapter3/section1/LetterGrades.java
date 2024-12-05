package com.ali.algojava.chapter3.section1;

import edu.princeton.cs.algs4.ST;
import edu.princeton.cs.algs4.StdOut;

// 3.1.1
public class LetterGrades {
  private ST<String, Double> gpa = new ST<>();

  public LetterGrades() {
    gpa.put("A+", 4.33);
    gpa.put("A", 4.00);
    gpa.put("A-", 3.67);
    gpa.put("B+", 3.33);
    gpa.put("B", 3.00);
    gpa.put("B-", 2.67);
    gpa.put("C+", 2.33);
    gpa.put("C", 2.00);
    gpa.put("C-", 1.67);
    gpa.put("D", 1.00);
    gpa.put("F", 0.00);
  }

  public boolean contains(String grade) {
    return gpa.contains(grade);
  }

  public double calcGPA(String[] grades) {
    double result = 0.0;
    for (String grade : grades) {
      if (!gpa.contains(grade)) {
        throw new RuntimeException("grade not valid");
      }
      result += gpa.get(grade);
    }
    return result / grades.length;
  }

  public static void main(String[] args) {

    LetterGrades lg = new LetterGrades();
    double gpa = lg.calcGPA(args);
    StdOut.printf("GPA: %f\n", gpa);
  }

}
