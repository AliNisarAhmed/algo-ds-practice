class Solution:

    def lowestCommonAncestor(self, root, p, q):

        p_val = p.val
        q_val = q.val

        node = root

        while node:

            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
