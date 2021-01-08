class Vertex {
	constructor(value, vertices = []) {
		this.value = value;
		this.adjacentVertices = vertices;
	}

	addAdjacentVertex(v) {
		if (
			!this.adjacentVertices.filter((iv) => iv.value === v.value).length > 0
		) {
			// if a vertex is not already in adjacent vertices
			// add it to the current vertex,
			// and also add the current vertex to the list of adjacent vertices of the other.
			// So that the graph is a CONNECTED Graph
			this.adjacentVertices.push(v);
			v.addAdjacentVertex(this);
		}

		return this;
	}
}

function dfsTraverse(vertex, visited = {}) {
	visited[vertex.value] = true;

	console.log('Vertex visited: ', vertex.value);

	for (let v of vertex.adjacentVertices) {
		if (!visited[v.value]) {
			dfsTraverse(v, visited);
		}
	}
}

function dfs(start, target, visited = {}) {
	visited[start.value] = true;

	console.log('Visited: ', start);

	if (start.value === target.value) {
		console.log('Found: ');
		return true;
	}

	for (let v of start.adjacentVertices) {
		if (!visited[v.value]) {
			const rest = dfs(v, target, visited);
			if (rest) {
				return rest;
			}
		}
	}

	return false;
}

function bfsTraverse(start) {
	let visited = {};
	let queue = [];
	console.log('Visited: ', start.value);
	visited[start.value] = true;
	queue.push(start);

	while (queue.length > 0) {
		let first = queue.shift();
		for (let n of first.adjacentVertices) {
			if (!visited[n.value]) {
				console.log('Visited: ', n.value);
				visited[n.value] = true;
				queue.push(n);
			}
		}
	}
}

function bfs(start, target) {
	let visited = {};
	let queue = [];
	console.log('Visited: ', start.value);
	visited[start.value] = true;
	queue.push(start);

	while (queue.length > 0) {
		let first = queue.shift();
		if (first.value === target.value) {
			return target.value;
		}
		for (let n of first.adjacentVertices) {
			if (!visited[n.value]) {
				console.log('Visited; ', n.value);
				visited[n.value] = true;
				queue.push(n);
			}
		}
	}

	return null;
}

function shortestPath(start, target) {
	let visited = {};
	let queue = [];
	let paths = {};

	console.log('Visited: ', start.value);
	visited[start.value] = true;
	queue.push(start);

	while (queue.length > 0) {
		let first = queue.shift();
		if (first.value === target.value) {
			break;
		}

		for (let n of first.adjacentVertices) {
			if (!visited[n.value]) {
				console.log('Visited: ', n.value);
				visited[n.value] = true;
				queue.push(n);
				paths[n.value] = first.value;
			}
		}
	}

	let path = [];
	let currentCityName = target.value;

	while (currentCityName !== start.value) {
		path.push(currentCityName);
		currentCityName = paths[currentCityName];
	}

	path.push(start.value);
	return path.reverse();
}

let a = new Vertex('Alice'),
	b = new Vertex('Bob'),
	c = new Vertex('Candy'),
	d = new Vertex('Derek'),
	e = new Vertex('Elaine'),
	f = new Vertex('Fred'),
	g = new Vertex('Gina'),
	h = new Vertex('Helen'),
	i = new Vertex('Irena');

a.addAdjacentVertex(b)
	.addAdjacentVertex(c)
	.addAdjacentVertex(d)
	.addAdjacentVertex(e);
b.addAdjacentVertex(f);
c.addAdjacentVertex(h);
d.addAdjacentVertex(e).addAdjacentVertex(g);
f.addAdjacentVertex(h);
g.addAdjacentVertex(i);

// dfsTraverse(a)

// console.log(dfs(a, i));

// bfsTraverse(a);

// console.log(bfs(a, i));

let idris = new Vertex('Idris'),
	kamil = new Vertex('Kamil'),
	lina = new Vertex('Lina'),
	sasha = new Vertex('Sasha'),
	marco = new Vertex('Marco'),
	ken = new Vertex('Ken'),
	talia = new Vertex('Talia');

idris.addAdjacentVertex(kamil).addAdjacentVertex(talia);
kamil.addAdjacentVertex(lina);
lina.addAdjacentVertex(sasha);
sasha.addAdjacentVertex(marco);
marco.addAdjacentVertex(ken);
ken.addAdjacentVertex(talia);

console.log(shortestPath(idris, lina));