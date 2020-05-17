const PriorityQueue = require('../Binary Heaps/priorityQueue');

class WeightedGraph {
	constructor() {
		this.adjacencyList = {};
	}

	addVertex(vertex) {
		if (!this.adjacencyList[vertex]) {
			this.adjacencyList[vertex] = [];
		}
		return this;
	}

	addEdge(v1, v2, weight) {
		this.adjacencyList[v1].push({ node: v2, weight });
		this.adjacencyList[v2].push({ node: v1, weight });
		return this;
	}

	// other methods can be implemented just like unweighted graph

	// Djikstra's Algorithm
	shortestPath(start, end) {
		const visited = [];

		const distances = {};
		Object.keys(this.adjacencyList).forEach((k) => {
			if (k === start) {
				distances[k] = 0;
			} else {
				distances[k] = Infinity;
			}
		});

		const pq = new PriorityQueue();
		Object.entries(distances).forEach(([k, v]) => pq.enqueue(k, v));

		const previous = {};
		Object.keys(distances).forEach((k) => (previous[k] = null));

		while (pq.values.length > 0) {
			const current = pq.extractMax();
			// visited.push(current.value);
			if (current.value === end) {
				visited.push(current.value);
				return visited;
			}
			const unvisited = this.adjacencyList[current.value].filter(
				(v) => !visited.includes(v.node)
			);

			// if the current node is not the end, and it does not have any unvisited neighbours
			// that means it is a DEAD END, it must not be added to the visited.
			if (unvisited.length > 1) {
				visited.push(current.value);
			}

			unvisited.forEach(({ node, weight }) => {
				let newDistance = distances[current.value] + weight;
				if (newDistance < distances[node]) {
					distances[node] = newDistance;
					previous[node] = current.value;
					pq.enqueue(node, weight);
				}
			});
		}
	}
}

const g = new WeightedGraph();

g.addVertex('a')
	.addVertex('b')
	.addVertex('c')
	.addVertex('d')
	.addVertex('e')
	.addVertex('f');

g.addEdge('a', 'c', 2)
	.addEdge('a', 'b', 4)
	.addEdge('b', 'e', 3)
	.addEdge('e', 'd', 3)
	.addEdge('e', 'f', 1)
	.addEdge('d', 'f', 1)
	.addEdge('d', 'c', 2)
  .addEdge('f', 'c', 4);

const x = new WeightedGraph();

x.addVertex('h')
  .addVertex('a')
  .addVertex('b')
  .addVertex('c')
  .addVertex('d')
  .addVertex('e')
  .addVertex('f')
  .addVertex('w')

x.addEdge('h', 'a', 3)
  .addEdge('h', 'b', 2)
  .addEdge('h', 'c', 5)
  .addEdge('c', 'e', 2)
  .addEdge('b', 'd', 1)
  .addEdge('b', 'e', 6)
  .addEdge('d', 'a', 3)
  .addEdge('d', 'f', 4)
  .addEdge('f', 'w', 2)
  .addEdge('f', 'e', 1)
	.addEdge('e', 'w', 4)

const y = new WeightedGraph();

y.addVertex('a')
y.addVertex('b')
y.addVertex('c')
y.addVertex('d')
y.addVertex('e')

y.addEdge('a', 'c', 3);
y.addEdge('a', 'b', 7);
y.addEdge('c', 'b', 1);
y.addEdge('a', 'c', 3);
y.addEdge('b', 'd', 2);
y.addEdge('b', 'e', 6);
y.addEdge('d', 'c', 2);
y.addEdge('d', 'e', 4);


console.log(g.shortestPath('a', 'f'))
console.log(x.shortestPath('h', 'w'));
console.log(y.shortestPath('a', 'e'))
