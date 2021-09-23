

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
      
      levels[level].push(current);

      if (current.left) {
        queue.unshift(current.left);
      }
      if (current.right) {
        queue.unshift(current.right);
      }
    }

    for (let i = 0; i < levels[level].length - 1; i++) {
      let current = levels[level][i];
      let next = levels[level][i] || null;
      current.next = next;
    }

    level++;
  }


  return root;
}
