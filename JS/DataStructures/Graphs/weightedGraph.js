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
			visited.push(current.value);
			if (current.value === end) return visited;
			const unvisited = this.adjacencyList[current.value].filter(
				(v) => !visited.includes(v.node)
			);

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

console.log(x.shortestPath('h', 'w'));
