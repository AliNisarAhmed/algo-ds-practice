from ..chap9.adaptable_pq import AdaptableHeapPriorityQueue


class Vertex:
    """Lightweight vertex structure for a graph"""
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """Do not call constructor directly, use Graph's insert_edge(u, v, x) instead"""

        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    """Representation of a simple graph using an adjacency map"""

    def __init__(self, directed=False):
        self._outgoing = {}

        # only create second map for directed graph, use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """this property is based on the original declaration of the graph, not its contents"""
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)

        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Return the number of (outgoing) edges incident to vertex v
        in the graph

        If graph is directed, optional parameter used to count incoming
        edges
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph"""

        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x"""
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e


def topological_sort(g: Graph):
    """
    Return a list of vertices of directed acyclic graph g in topological order

    If graph has a cycle, the result will be incomplete
    """

    topo = []  # a list of vertices placed in topological order
    ready = []  # list of vertices that have no remaining constraints
    incount = {}  # keep track of in-degree for each vertex

    for u in g.vertices():
        incount[u] = g.degree(u, False)  # False = incoming degree
        if incount[u] == 0:
            # if u has not incoming edges, it is free of constraints
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)  # add u to topological order
        # consider all outgoing neighbors of u
        for e in g.incident_edges(u):
            v = e.opposite(u)
            # v has one less constraint w/o u
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo


def shortest_path_lengths(g: Graph, src: Vertex):
    """
    Djikstra's algorithm

    Compute shortest-path distances from src to reachable vertices of g

    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e, weight > 0

    Return dictionary mapping each reachable vertex to its distance from src
    """

    d = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}  # map from vertex to its pq-locator returned by AdaptableHeapPriorityQueue

    # for each vertex v of the graph, add an entry to the PQ
    # with the source distance 0 and all others having Infinity distance

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        del pqlocator[u]  # u is no longer in PQ

        for e in g.incident_edges(u):  # outgoing edges (u, v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u, v)
                weight = e.element()
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    pq.update(pqlocator[v], d[v], v)
    return cloud


def shortest_path_tree(g: Graph, s: Vertex, d):
    """
    Reconstruct shortest-path tree rooted at vertex s
    given distance map d (output of shortest_path_lengths)

    Return tree as a map from each reachable vertex v (other than s)
    to the edge e=(u,v) that is used to reach v from its parent u in
    the tree
    """

    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):  # False = incoming edges
                u = e.opposite(v)
                weight = e.element()
                if d[v] == d[u] + weight:
                    tree[v] = e  # edge e is used to reach v
    return tree
