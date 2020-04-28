class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(value) {
    let newNode = new Node(value);
    if (!this.root) {
      this.root = newNode;
    } else {
      let current = this.root;
      while(true) {
        if (value < current.value) {
          if (!current.left) {
            current.left = newNode;
            return this;
          } else {
            current = current.left;
          }
        } else {
          if (!current.right) {
            current.right = newNode;
            return this;
          } else {
            current = current.right;
          }
        }
      }
    }
  }

  insert2(value) {
    let newNode = new Node(value);
    if (!this.root) {
      this.root = newNode;
      return this;
    } else {
      this.insertR(this.root, newNode);
      return this;
    }
  }

  insertR(current, newNode) {
    if (newNode.value < current.value) {
      if (current.left === null) {
        current.left = newNode;
      } else {
        this.insertR(current.left, newNode);
      }
    } else {
      if (current.right === null) {
        current.right = newNode;
      } else {
        this.insertR(current.right, newNode);
      }
    }
  }

  find(value) {
    if (!this.root) {
      return false;
    }
    return this.findR(this.root, value);
  }

  findR(current, v) {
    if (current === null)
      return false;
    if (current.value === v)
      return true;
    if (v > current.value)
      return this.findR(current.right, v);

    return this.findR(current.left, v);
  }

  // iterative
  find2(value) {
    if (!this.root)
      return false;
    let current = this.root;
    while(true) {
      if (!current)
        return false;
      if (current.value === value)
        return true;
      if (value > current.value)
        current = current.right;
      if (value < current.left)
        current = current.left;
    }
  }
}

const bst = new BST();
bst.insert2(10);
bst.insert2(12);

module.exports = BST;