// Generic Tree 


class Tree {
  constructor(value) {
    this.value = value;
    this.children = [];
  }
  insertChild(value) {}

  // Uses a Depth-First Traversal
  // static traverse(tree, func = console.log) {}

  contains(searchValue) {}

  static size(tree) {}

  static find(tree, value) {}

  insert(parentTree, value) {
    const newTree = new Tree(value);
    parentTree.children.push(newTree);
    return newTree;
  }

  remove(value) {
    this.children = this.children.filter((v) => v.value !== value);
  }

  reorder(node1, node2) {}
}

// Above tree adopted to Chatbot - where a node is a question, with yes or no answer
// a left in this tree is a recommendation by the bot

class BOTTree {
  constructor(question) {
    this.question = question;
    this.yes = null;
    this.no = null;
  }

  traverse(func = console.log) {
    func(this.question); 
    if (this.yes) this.yes.traverse(func);
    if (this.no) this.no.traverse(func);
  }

  insertChild(question, side = 'yes') {
    const newQ = new BOTTree(question);
    this[side] = newQ;
    return newQ;
  }

  removeChild() {}
}

