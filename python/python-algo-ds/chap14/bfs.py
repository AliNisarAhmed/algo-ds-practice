from .graph import Graph, Vertex
from typing import Dict


def BFS(g: Graph, s: Vertex, discovered: Dict):
    """Perform BFS of the undiscovered portion of g starting at s

    `discovered` is a dictionary mapping each vertex to the edge that
    was used to discover it during BFS (s should be mapped to None prior to
    the call).

    Newly discovered vertices will be added to the dictionary as a result
    """

    level = [s]  # first level only includes s
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:
                    # v is an unvisited vertex
                    discovered[v] = e  # e is the tree edge that discovered v
                    # v will be further considered in the next path
                    next_level.append(v)
        level = next_level
