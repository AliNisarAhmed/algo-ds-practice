// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
//


// Iterative 
//
function isSymmetric(root) {
  let queue = [];
  queue.push(root);
  queue.push(root);

  while (queue.length > 0) {
    let t1 = queue.shift();
    let t2 = queue.shift();

    if (t1 === null && t2 === null) continue;
    if (t1 === null || t2 === null) return false;
    if (t1.val !== t2.val) return false;

    queue.push(t1.left);
    queue.push(t2.right);

    queue.push(t1.right);
    queue.push(t2.left);
  }

  return true;
}




 // Recursive
function isSymmetric(root) {
  if (!root) return true;

  return isSymmetricBinary(root.left, root.right);
}

function isSymmetricBinary(left, right) {
  if (!left && !right) return true;

  if (left && !right) return false;

  if (!left && right) return false;

  if (left.val !== right.val) return false;

  return isSymmetricBinary(left.left, right.right) && isSymmetricBinary(left.right, right.left);
}
