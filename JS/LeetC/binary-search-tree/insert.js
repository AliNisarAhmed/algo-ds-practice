function insert(node, val) {
  let newNode = { val, left: null, right: null };
  if (!node) return newNode;

  if (val > node.val) {
    if (!node.right) {
      node.right = newNode;
      return this;
    }
    return insert(node.right, val);
  } else {
    if (!node.left) {
      node.left = newNode;
      return this;
    }

    return insert(node.left, val);
  }
}
