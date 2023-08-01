"""
A Red-Black tree is a BST with nodes colored wither red or black with the following properties:
    - Root Property:
        The root is black
    - Red Property: 
        The children of a red node (if any) are black
    - Depth Property:
        All noes with 0 or 1 children have the same `black depth`,
            defined as the number of black ancestors (including itself)

Wikipedia defines the Red-Black tree properties as follows:
    - Every node is either Red or Black
    - All NIL (empty child nodes of external nodes) are considered black
    - a red node does not have a red child
    - Every path from a node to its descendent NIL node goes thru the same number of black nodes
    - if a node has exactly 1 child, it must be red

Relation with (2,4) trees:
    - a Red-Black tree can be converted to a (2,4) tree by merging every red node w into its parent,
        storing the entry from w at its parent, 
        and with the children of w becoming ordered children of the parent


Proposition: The height of a Red-Black tree storing n entries is O(log n)
"""
