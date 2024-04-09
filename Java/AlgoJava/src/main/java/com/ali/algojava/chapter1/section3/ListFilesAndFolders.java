package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;
import java.io.File;

// 1.3.43
public class ListFilesAndFolders {
  private static String path = "/home/aa87/delete_me";

  private static Queue<File> q = new Queue<>();

  public static void main(String[] args) {
    if (args.length == 1) {
      path = args[0];
    }

    listFiles(new File(path), 0);
  }

  private static void listFiles(File file, int depth) {
    if (file.isFile()) {
      printFile(file, depth);
    } else {
      printDir(file, depth);
      File[] children = file.listFiles();
      if (children != null) {
        for (File child : children) {
          listFiles(child, depth + 2);
        }
      }
    }
  }

  private static void printFile(File file, int level) {
    StdOut.println(" ".repeat(level * 2) + file.getName());
  }

  private static void printDir(File dir, int level) {
    StdOut.println(" ".repeat(level * 2) + dir.getName() + "/");
  }
}
