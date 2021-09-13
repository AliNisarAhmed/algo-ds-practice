// inorder: left - root - right
// postorder: left - right - root

class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function buildTree(inOrder, postOrder) {
  let leftIndex = 0;
  let rightIndex = postOrder.length - 1;

  let tree;

  while (inOrder[leftIndex] !== postOrder[rightIndex]) {
    let node = new TreeNode(postOrder[rightIndex]);
    node.left = inOrder[leftIndex];
    node.right = postOrder[rightIndex];

    if (tree) {
      tree.left = node.left;
      tree.right = node.right;
    } else {
      tree = node;
    }

    leftIndex += 2;
    rightIndex -= 2;
  }

  return tree;
}
