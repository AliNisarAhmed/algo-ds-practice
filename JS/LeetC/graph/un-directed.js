

class Vertex {
  constructor(value) {
    this.val = value;
    this.adjacentVertices = [];
  }

  addAdjacent(node) {
    if (this.adjacentVertices.includes(node)) return;
    this.adjacentVertices.push(node);
    node.addAdjacent(this);
  }

}

function depthFirst(vertex, visited = {}) {
  visited[vertex.val] = true;

  console.log('Visited: ', vertex.val);

  vertex.adjacentVertices.forEach(v => {
    if (!visited[v.val]) {
      depthFirst(v, visited);
    }
  })
}

function breadthFirst(vertex) {
  let queue = [];
  let visited = {};

  queue.push(vertex);

  while (queue.length > 0) {
    let current = queue.shift();

    if (!visited[current.val]) {
      visited[current.val] = true;
      console.log('Visited: ', current.val);

      for (let v of current.adjacentVertices) {
        queue.push(v);
      }
    }
  }
}

let alice = new Vertex('alice');
let bob = new Vertex('bob');
let candy = new Vertex('candy');
let derek = new Vertex('derek');
let elaine = new Vertex('elaine');
let fred = new Vertex('fred');
let gina = new Vertex('gina');
let helen = new Vertex('helen');
let irena = new Vertex('irena');


alice.addAdjacent(bob);
alice.addAdjacent(candy);
alice.addAdjacent(derek);
alice.addAdjacent(elaine);

bob.addAdjacent(fred);

candy.addAdjacent(helen);

derek.addAdjacent(elaine);
derek.addAdjacent(gina);

helen.addAdjacent(fred);
helen.addAdjacent(candy);

irena.addAdjacent(gina);

depthFirst(alice);

console.log('-------------');

breadthFirst(alice);
