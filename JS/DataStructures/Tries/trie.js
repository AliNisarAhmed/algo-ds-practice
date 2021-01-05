class Node {
	constructor() {
		this.children = {};
	}
}

class Trie {
	constructor() {
		this.root = new Node();
	}

	search(str) {
		let currentNode = this.root;
		for (let c of str) {
			if (currentNode.children[c]) {
				currentNode = currentNode.children[c];
			} else {
				return null;
			}
		}
		return currentNode;
	}

	insert(str) {
		let currentNode = this.root;
		for (let c of str) {
			if (currentNode.children[c]) {
				currentNode = currentNode.children[c];
			} else {
				currentNode.children[c] = new Node();
				currentNode = currentNode.children[c];
			}
		}
		currentNode.children['*'] = null;
		return this;
	}

	collectAllWords(node = null, word = "", words = []) {
		let currentNode = node ? node : this.root;

		for (let [key, value] of Object.entries(currentNode.children)) {
			if (key === "*") {
				words.push(word);
			} else {
				this.collectAllWords(value, word + key, words);
			}
		}

		return words;
	}

	autoComplete(prefix) {
		let currentNode = this.search(prefix);
		if (!currentNode) {
			return null;
		}
		return this.collectAllWords(currentNode)
	}

	printKeys(currentNode = this.root) {
		for (let [k,v] of Object.entries(currentNode.children)) {
			console.log(k);
			if (v) {
				this.printKeys(v);
			}
		}
	}

	autoCorrect(prefix) {
		let [p, node] = this.searchTill(prefix);
		if (p === prefix) {
			return [p];
		}

		return this.collectAllWords(node).map(w => p + w);
	}

	searchTill(prefix) {
		let currentNode = this.root;
		for (let [index, c] of [...prefix].entries()) {
			if (currentNode.children[c] === undefined || currentNode.children[c] === null) {
				return [prefix.substring(0, index), currentNode];
			} else {
				currentNode = currentNode.children[c];
			}
		}
		return [prefix, currentNode];
	}

	autoCorrect2(prefix) {
		let currentNode = this.root;
		let wordSoFar = '';

		for (let c of prefix) {
			if (currentNode.children[c]) {
				wordSoFar += c;
				currentNode = currentNode.children[c];
			} else {
				return this.collectAllWords(currentNode).map(w => wordSoFar + w);
			}
		}
		return prefix;
	}
}

let tr = new Trie();
tr.insert('ace')
	.insert('act')
	.insert('bad')
	.insert('bake')
	.insert('batter')
	.insert('cab')
	.insert('catnap')
	.insert('catnip');