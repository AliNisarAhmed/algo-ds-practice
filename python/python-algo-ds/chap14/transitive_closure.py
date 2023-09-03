from .graph import Graph
from copy import deepcopy


def floyd_warshall(g: Graph):
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)

    for k in range(n):
        for i in range(n):
            # verify that edge (i, k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k, j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[k]) is not None:
                        # if (i, j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure
