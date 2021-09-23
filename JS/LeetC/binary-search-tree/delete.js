function deleteNode(node, val) {
  if (!node) return node;

  if (val > node.val) {
    node.right = deleteNode(node.right, val);
    return node;
  } else if (val < node.val) {
    node.left = deleteNode(node.left, val);
    return node;
  } else if (val === node.val) {
    if (!node.left) {
      return node.right;
    } else if (!node.right) {
      return node.left;
    } else {
      node.right = lift(node.right, node);
      return node;
    }
  }
}

function lift(node, nodeToDelete) {
  if (node.left) {
    node.left = lift(node.left, nodeToDelete);
    return node;
  } else {
    nodeToDelete.val = node.val;
    return node.right;
  }
}
