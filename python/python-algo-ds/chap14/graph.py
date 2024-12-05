from chap9.adaptable_pq import AdaptableHeapPriorityQueue, HeapPriorityQueue
from .partition import Partition
import pprint


class Vertex:
    """Lightweight vertex structure for a graph"""
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))

    def __repr__(self):
        return repr(self._element)


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

    def __repr__(self):
        return repr(self._origin) + '-' + repr(self._destination)


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
        """insert_edge(origin, destination, weight)"""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


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
    given distance map d (output of shortest_path_lengths/Djikstra's)

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


def MST_PrimJarnik(g: Graph):
    """Compute a min spanning tree of weighted graph g

    Return a list of edges that comprise the MST (in arbitrary order)
    """

    d = {}  # d[v] is bound on distance to tree
    tree = []  # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()  # d[v] maps to value (v, e=(u,v))
    pqlocator = {}  # map from vertex to its pq locator

    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value
        del pqlocator[u]  # u is no longer in pq

        if edge is not None:
            tree.append(edge)

        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:  # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                weight = link.element()
                if weight < d[v]:
                    d[v] = weight
                    pq.update(pqlocator[v], d[v], (v, link))
    return tree


def MST_Kruskal(g: Graph):
    """Compute a min spanning tree of a graph

    Return a list of edges that comprise the MST

    The elements of the grah's edges are assumed to be weights
    """
    tree = []  # list of edges in the MST
    pq = HeapPriorityQueue()  # entries are edges in G, with weights as keys
    forest = Partition()  # keeps track of forest of clusters
    position = {}  # map each node to its partition key

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)  # edge's element is assumed to be its weight

    size = g.vertex_count()

    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
    return tree


if __name__ == "__main__":
    g = Graph()
    jfk = g.insert_vertex('JFK')
    pvd = g.insert_vertex("PVD")
    bos = g.insert_vertex("BOS")
    bwi = g.insert_vertex("BWI")
    mia = g.insert_vertex("MIA")
    ord = g.insert_vertex("ORD")
    dfw = g.insert_vertex("DFW")
    sfo = g.insert_vertex("SFO")
    lax = g.insert_vertex("LAX")

    g.insert_edge(bwi, jfk, 184)
    g.insert_edge(bwi, ord, 621)
    g.insert_edge(bwi, mia, 946)
    g.insert_edge(jfk, dfw, 1391)
    g.insert_edge(jfk, pvd, 144)
    g.insert_edge(jfk, ord, 740)
    g.insert_edge(jfk, mia, 1090)
    g.insert_edge(jfk, bos, 187)
    g.insert_edge(pvd, ord, 849)
    g.insert_edge(bos, mia, 1258)
    g.insert_edge(bos, sfo, 2704)
    g.insert_edge(bos, ord, 867)
    g.insert_edge(mia, dfw, 1121)
    g.insert_edge(mia, lax, 2342)
    g.insert_edge(dfw, ord, 802)
    g.insert_edge(dfw, sfo, 1464)
    g.insert_edge(dfw, lax, 1235)
    g.insert_edge(lax, sfo, 337)
    g.insert_edge(sfo, ord, 1846)

    d = shortest_path_lengths(g, bwi)
    pprint.pprint(d)
    pprint.pprint(shortest_path_tree(g, bwi, d))

    pprint.pp(MST_PrimJarnik(g))


# R-14.2
# If G is a simple undirected graph with 12 vertices and 3 connected components
# what is the largest number of edges it might have?
# Answer: 45 (1 component with 10 vertices, 2 components with 1 vertex each)


# R-14.6
# Answer:
# When we insert, we just append to end of vertices list which is O(1)
# When we remove a vertex, we must search for all `m` edges to ensure
# no edge is left with that vertex


# R-14.9 & R-14.10
# Without Edge list, it will not be possible to maintain time bounds, esp
# the edges() method, since we will need to loop through each vertex to get all
# edges, thus converting it to O(n + m)

# R-14.11
# a -> Adj. List  => since it uses O(n + m) space vs Adj.Matrix which uses O(n^2)
# b -> Adj.Matrix => since n is much greater than m, space usage for both is equivalent
#       while the O(1) access for Adj.Matrix will become important
#     However, we can also use Adj.List as space usage is equivalent, and it provides
#     much better time for `insert_vertex` and `remove_vertex`
# c -> Adj.Matrix => O(1) for get_edge(u, v) in worst case, cannot be beat


# R-14.14
# The DFS traversal of a complete tree looks like a path (since all edges connect to each other)

# R-14.15
# The BFS looks like a star, i.e., a rooted tree with 1 root and all external nodes


# R-14-16
# b => 1 - 2 - 3 - 4 - 6 - 5 - 7 - 8
# c => 1 - 2 - 3 - 4 - 6 - 5 - 7 - 8

# R-14.22
# To determine the course order, use topological sorting


# R-14.27
# 120 - 170 - 115 - 155 - 175 - 180 - 175
# (1-8) - (8-5) - (5-3) - (8-2) - (2-4) - (2-6) - (6-7)
