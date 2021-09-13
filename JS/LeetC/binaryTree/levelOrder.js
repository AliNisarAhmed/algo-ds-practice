// Level Order - aka - Breadth First Search
//

// Iterative - Use a queue
//
function levelOrder(root) {
  let levels = [];

  if (!root) return levels;

  let queue = [];
  let level = 0;

  queue.unshift(root);

  while (queue.length > 0) {
    levels.push([]);

    let levelLength = queue.length;

    for (let i = 0; i < levelLength; i++) {
      let current = queue.pop();
      
      levels[level].push(current.val);

      if (current.left) {
        queue.unshift(current.left);
      }
      if (current.right) {
        queue.unshift(current.right);
      }
    }

    level++;
  }

  return levels;
}


function levelOrder(root) {
  let levels = [];

  if (!root) {
    return levels;
  }

  helper(root, 0);
  return levels;

  function helper(node, level) {
    if (levels.length === level) {
      levels.push([]);
    }

    levels[level].push(node.val);

    if (node.left) {
      helper(node.left, level + 1);
    }

    if (node.right) {
      helper(node.right, level + 1);
    }
  }
}
