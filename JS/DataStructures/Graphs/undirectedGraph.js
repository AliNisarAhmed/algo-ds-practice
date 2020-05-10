// Undirected Graph implemented using Adjacency List
  // (Object with Key are vertex and arrays for Edges)

class UDGraph {
	constructor() {
		this.adjacencyList = {};
	}

	addVertex(name) {
		if (!this.adjacencyList[name]) {
			this.adjacencyList[name] = [];
		}
	}

	addEdge(vertex1, vertex2) {
		this.adjacencyList[vertex1].push(vertex2);
		this.adjacencyList[vertex2].push(vertex1);
	}

	removeEdge(v1, v2) {
		this.adjacencyList[v1] = this.adjacencyList[v1].filter((v) => v !== v2);
		this.adjacencyList[v2] = this.adjacencyList[v2].filter((v) => v !== v1);
	}

	removeVertex(v) {
		this.adjacencyList[v].forEach((e) => {
			this.adjacencyList[e] = this.adjacencyList[e].filter((k) => k !== v);
		});
		delete this.adjacencyList[v];
	}

	dftRecursive(v) {
		const result = [];
		const visited = {};

		const helper = (v) => {
			if (!v) return;
			visited[v] = true;
			result.push(v);
			for (let n of this.adjacencyList[v]) {
				if (!visited[n]) {
					helper(n);
				}
			}
		}

		helper(v);

		return result;
	}

	dftIterative(v) {
		const stack = [];
		const result = [];
		const visited = {};

		stack.push(v);
		visited[v] = true;

		while (stack.length > 0) {
			const next = stack.pop();
			result.push(next);
			this.adjacencyList[next].forEach(n => {
				if (!visited[n]) {
					stack.push(n);
					visited[n] = true;
				}
			})
		}

		return result;
	}

	bftIterative(v) {
		const queue = [];
		const result = [];
		const visited = {};

		queue.push(v);
		visited[v] = true;

		while (queue.length > 0) {
			const next = queue.shift();
			result.push(next);

			this.adjacencyList[next].forEach(n => {
				if (!visited[n]) {
					queue.push(n);
					visited[n] = true;
				}
			})
		}

		return result;

	}
}

let g = new UDGraph();

g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')

g.addEdge('A', 'B');
g.addEdge('A', 'C');
g.addEdge('D', 'B');
g.addEdge('C', 'E');
g.addEdge('D', 'E');
g.addEdge('D', 'F');
g.addEdge('E', 'F');

console.log(g.dftRecursive('A'));
console.log(g.dftIterative('A'));
console.log(g.bftIterative('A'));