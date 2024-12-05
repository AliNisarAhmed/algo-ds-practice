/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

import type { TreeNode } from "./00-TreeNode";

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) {
    return true;
  }

  if (!root.left && !root.right) {
    return true;
  }

  if (root.left && !root.right) {
    return false;
  }

  if (root.right && !root.left) {
    return false;
  }

  return compare(root.left!, root.right!);
}

function compare(
  nodeLeft: TreeNode | null,
  nodeRight: TreeNode | null,
): boolean {
  if (nodeLeft && !nodeRight) {
    return false;
  }

  if (nodeRight && !nodeLeft) {
    return false;
  }

  if (!nodeLeft && !nodeRight) {
    return true;
  }
  return (
    nodeLeft?.val === nodeRight?.val &&
    compare(nodeLeft!.left, nodeRight!.right) &&
    compare(nodeLeft!.right, nodeRight!.left)
  );
}


// Iterative
function isSymmetricIter(root: TreeNode | null): boolean {
    if (!root) {
      return true;
    }
    let q: Array<TreeNode | null> = [root.left, root.right];
    while (q.length !== 0) {
        let t1: TreeNode | null = q.shift() ?? null;
        let t2: TreeNode | null = q.shift() ?? null;
        if (t1 === null && t2 === null) {
            continue;
        }
        if (t1 === null || t2 === null) {
            return false;
        }
        if (t1.val !== t2.val) {
            return false;
        }
        q.push(t1.left, t2.right, t1.right, t2.left);
    }
    return true;
}
