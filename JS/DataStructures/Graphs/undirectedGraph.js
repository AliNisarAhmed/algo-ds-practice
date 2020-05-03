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
}

let g = new UDGraph();

g.addVertex('Hong Kong');
g.addVertex('Karachi');
g.addVertex('Edmonton');
g.addVertex('Calgary');
g.addVertex('Toronto');
g.addVertex('Seattle');

g.addEdge('Edmonton', 'Calgary');
g.addEdge('Calgary', 'Toronto');
g.addEdge('Edmonton', 'Toronto');
g.addEdge('Edmonton', 'Hong Kong');
g.addEdge('Edmonton', 'Karachi');
g.addEdge('Calgary', 'Karachi');
g.addEdge('Toronto', 'Karachi');

g.removeVertex('Edmonton');
