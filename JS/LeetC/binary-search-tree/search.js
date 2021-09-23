function search(node, target) {
  if (!node || node.val === target) {
    return node;
  }

  if (target > node.val) {
    return search(node.right, target);
  }

  return search(node.left, target);
}
