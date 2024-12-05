package com.ali.algojava.chapter3.section2;

import com.ali.algojava.chapter1.section3.Queue;

public class BST<Key extends Comparable<Key>, Value> {
  private Node root;

  private class Node {
    private Key key;
    private Value val;
    private Node left, right;
    private int N; // nodes in subtree rooted here
    private int height; // height of this node

    public Node(Key key, Value val, int N, int height) {
      this.key = key;
      this.val = val;
      this.N = N;
      this.height = height;
    }

    public Node(Key key, Value val, int N) {
      this.key = key;
      this.val = val;
      this.N = N;
      this.height = 1;
    }
  }

  public int height() {
    return height(root);
  }

  private int height(Node x) {
    if (x == null) {
      return 0;
    }
    return x.height;
  }

  public int size() {
    return size(root);
  }

  private int size(Node x) {
    return x == null ? 0 : x.N;
  }

  public Value get(Key key) {
    return get(root, key);
  }

  private Value get(Node x, Key key) {
    if (x == null) {
      return null;
    }
    int cmp = key.compareTo(x.key);
    if (cmp < 0) {
      return get(x.left, key);
    } else if (cmp > 0) {
      return get(x.right, key);
    } else {
      return x.val;
    }
  }

  private Node getNode(Key key) {
    Node x = root;
    while (x != null) {
      int cmp = key.compareTo(x.key);
      if (cmp == 0) {
        return x;
      } else if (cmp < 0) {
        x = x.left;
      } else {
        x = x.right;
      }
    }
    return null;
  }

  public Value get_iter(Key key) {
    Node x = root;
    while (x != null) {
      int cmp = key.compareTo(x.key);
      if (cmp == 0) {
        return x.val;
      } else if (cmp < 0) {
        x = x.left;
      } else {
        x = x.right;
      }
    }
    return null;
  }

  public Node put(Key key, Value val) {
    if (root == null) {
      root = new Node(key, val, 0);
      return root;
    }
    return put(root, key, val);
  }

  public Node put(Node x, Key key, Value val) {
    if (x == null) {
      return new Node(key, val, 1);
    }
    int cmp = key.compareTo(x.key);
    if (cmp < 0) {
      x.left = put(x.left, key, val);
    } else if (cmp > 0) {
      x.right = put(x.right, key, val);
    } else {
      x.val = val;
    }
    x.N = size(x.left) + size(x.right) + 1;
    x.height = 1 + Math.max(height(x.left), height(x.right));
    return x;
  }

  // 3.2.13
  public Node put_iter(Key key, Value val) {
    Node current = root;

    while (current != null) {
      int cmp = key.compareTo(current.key);
      if (cmp < 0) {
        current = current.left;
      } else if (cmp > 0) {
        current = current.right;
      } else {
        current.val = val;
        return current;
      }
    }

    // second pass
    if (root == null) {
      root = new Node(key, val, 1);
      return root;
    }

    current = root;
    while (true) {
      int cmp = key.compareTo(current.key);
      current.N += 1;
      if (cmp < 0) {
        if (current.left != null) {
          current = current.left;
        } else {
          current.left = new Node(key, val, 1);
          break;
        }
      } else if (cmp > 0) {
        if (current.right != null) {
          current = current.right;
        } else {
          current.right = new Node(key, val, 1);
          break;
        }
      }
    }
    return current;
  }

  public Key select_iter(int rank) {
    if (rank >= size()) {
      throw new IllegalArgumentException("rank provided is higher than tree size");
    }
    Node x = root;
    while (x != null) {
      int leftSubtreeSize = size(x.left);
      if (leftSubtreeSize == rank) {
        return x.key;
      } else if (leftSubtreeSize > rank) {
        x = x.left;
      } else {
        rank -= (leftSubtreeSize + 1);
        x = x.right;
      }
    }
    return null;
  }

  public Key min() {
    if (root == null) {
      return null;
    }
    return min(root).key;
  }

  private Node min(Node x) {
    if (x.left == null) {
      return x;
    }
    return min(x.left);
  }

  // 3.2.14
  public Key min_iter() {
    if (root == null) {
      return null;
    }
    Node x = root;
    while (x.left != null) {
      x = x.left;
    }
    return x.key;
  }

  public Key max() {
    return max(root).key;
  }

  private Node max(Node x) {
    if (x.right == null) {
      return x;
    }
    return max(x.right);
  }

  public Key floor(Key key) {
    Node x = floor(root, key);
    if (x == null) {
      return null;
    }
    return x.key;
  }

  private Node floor(Node x, Key key) {
    if (x == null) {
      return null;
    }
    int cmp = key.compareTo(x.key);
    if (cmp == 0) {
      return x;
    }
    if (cmp < 0) {
      // if given key is less than node's key, the floor must be on the left subtree
      return floor(x.left, key);
    }

    Node t = floor(x.right, key);
    if (t != null) {
      return t;
    } else {
      return x;
    }
  }

  public Key floor_iter(Key key) {
    Node x = root;
    Key currentFloor = null;
    while (x != null) {
      int cmp = key.compareTo(x.key);
      if (cmp == 0) {
        return x.key;
      } else if (cmp < 0) {
        x = x.left;
      } else {
        currentFloor = x.key;
        x = x.right;
      }
    }
    return currentFloor;
  }

  public Key select(int k) {
    return select(root, k).key;
  }

  private Node select(Node x, int k) {
    // return node containing key of rank k
    if (x == null) {
      return null;
    }

    int t = size(x.left);
    if (t > k) {
      return select(x.left, k);
    } else if (t < k) {
      return select(x.right, k - t - 1);
    } else {
      return x;
    }
  }

  public int rank(Key k) {
    return rank(k, root);
  }

  private int rank(Key key, Node x) {
    // return number of keys less than k in the subtree rooted at x
    if (x == null) {
      return 0;
    }

    int cmp = key.compareTo(x.key);
    if (cmp < 0) {
      return rank(key, x.left);
    } else if (cmp > 0) {
      return 1 + size(x.left) + rank(key, x.right);
    } else {
      return size(x.left);
    }
  }

  // 3.2.15
  public int rank_iter(Key key) {
    Node x = root;
    int rank = 0;
    while (x != null) {
      int cmp = key.compareTo(x.key);
      if (cmp < 0) {
        x = x.left;
      } else if (cmp > 0) {
        rank += size(x.left) + 1;
        x = x.right;
      } else {
        rank += size(x.left);
        return rank;
      }
    }
    return rank;
  }

  public void deleteMin() {
    root = deleteMin(root);
  }

  private Node deleteMin(Node x) {
    if (x.left == null) {
      return x.right;
    }
    x.left = deleteMin(x.left);
    x.N = size(x.left) + size(x.right) + 1;
    x.height = 1 + Math.max(height(x.left), height(x.right));
    return x;
  }

  public void delete(Key key) {
    root = delete(root, key);
  }

  private Node delete(Node x, Key key) {
    if (x == null) {
      return null;
    }

    int cmp = key.compareTo(x.key);
    if (cmp < 0) {
      x.left = delete(x.left, key);
    } else if (cmp > 0) {
      x.right = delete(x.right, key);
    } else {
      if (x.right == null) {
        return x.left;
      }
      if (x.left == null) {
        return x.right;
      }

      Node t = x;
      x = min(t.right);
      x.right = deleteMin(t.right);
      x.left = t.left;
    }
    x.N = size(x.left) + size(x.right) + 1;
    x.height = 1 + Math.max(height(x.left), height(x.right));
    return x;
  }

  public Iterable<Key> keys() {
    return keys(min(), max());
  }

  public Iterable<Key> keys(Key lo, Key hi) {
    Queue<Key> queue = new Queue<>();
    keys(root, queue, lo, hi);
    return queue;
  }

  private void keys(Node x, Queue<Key> queue, Key lo, Key hi) {
    if (x == null) {
      return;
    }
    int cmplo = lo.compareTo(x.key);
    int cmphi = hi.compareTo(x.key);

    // if our node is greater than lo, go to it's left subtree
    if (cmplo < 0) {
      keys(x.left, queue, lo, hi);
    }

    // if our node is between lo and hi, add it to queue
    if (cmplo <= 0 && cmphi >= 0) {
      queue.enqueue(x.key);
    }

    // if our node is less than hi, include it's right subtree
    if (cmphi > 0) {
      keys(x.right, queue, lo, hi);
    }
  }

  // 3.2.6
  public int height_rec() {
    return height_rec(root);
  }

  private int height_rec(Node x) {
    if (x == null) {
      return 0;
    }

    if (x.left == null && x.right == null) {
      return 1;
    }

    return 1 + Math.max(height_rec(x.left), height_rec(x.right));
  }
}

// 3.2.2
// A, C, E, H, R, S, X,
// 01 03 05 08 18 19 24 (asc)
//
// X, S, R, H, E, C, A,
// 24 19 18 08 05 03 01 (Desc)
//
// X, A, S, C, R, E, H
// 24 01 19 03 18 05 08
//
// X, A, S, C, R, H, E,
// 24 01 19 03 18 08 05
//
// A, X, C, S, E, H, R,
// 01 24 03 19 05 08 18
//

// 3.2.3
// A X C S E R H
// 8,19,18,24,3,5,1
// H S R X C E A

// 3.2.4
// d is not possible since 8 comes after 7 in it's left subtree
