class TrieNode {
  constructor() {
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  search(str) {
    let current = this.root;

    for (let c of str) {
      if (current.children[c]) {
        current = current.children[c];
      } else {
        return null;
      }
    }

    return current;
  }

  insert(str) {
    let current = this.root;
    for (let c of str) {
      if (!current.children[c]) {
        current.children[c] = new TrieNode();
      }
      current = current.children[c];
    }

    current.children["*"] = null;
    return this;
  }

  collectAllWords(node = null, word = "", words = []) {
    let current = node || this.root;

    for (let [key, value] of Object.entries(current.children)) {
      if (key === "*") {
        words.push(word);
      } else {
        this.collectAllWords(value, word + key, words);
      }
    }

    return words;
  }

  autoComplete(prefix) {
    let current = this.search(prefix);

    if (!current) {
      return null;
    }

    return this.collectAllWords(current);
  }

  autoCorrect(word) {
    let current = this.root;

    let wordSoFar = [];

    for (let c of word) {
      if (current.children[c] === "*") {
        // we found the full word
        return wordSoFar.join("");
      } else if (current.children[c]) {
        wordSoFar.push(c);
        current = current.children[c];
      } else {
        wordSoFar.join("") + this.collectAllWords(current)[0];
      }
    }
  }
}
