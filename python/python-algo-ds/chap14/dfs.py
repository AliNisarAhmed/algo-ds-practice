from .graph import Graph, Vertex
from typing import Dict


def DFS(g: Graph, u: Vertex, discovered: Dict):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u

    `discovered` is a dictionary mapping each vertex to the edge that was
    used to discover it during the DFS (`u` should be "discovered" prior
    to the call)
    Newly discovered vertices will be added to the dictionary as a result

    This function must be called like this:
        result = {u: None} # `u` is trivially already discovered
        DFS(g, u, result)
    """

    for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


def construct_path(u: Vertex, v: Vertex, discovered: Dict):
    path = []
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            # e is an edge connecting walk with opposite(walk)
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def DFS_complete(g: Graph):
    """Perform DFS for entire graph & return forest as a dictionary

    Result maps each vertex v to the edge that was used to discover it
    (Vertices that are roots of a DFS tree are mapped to None)
    """

    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)
    return forest
