// Bucket options: Array, LinkedList, BST (best) since it has O(log(n)) insert, removal, search

class MyHashSet {
  constructor() {
    this.keyRange = 769;
    this.data = Array.from({ length: this.keyRange });
  }

  _hash(x) {
    return x % this.keyRange;
  }

  add(key) {
    const hash = this._hash(key);
    const loc = this.data[hash];

    if (loc) {
      if (!loc.includes(key)) {
        loc.push(key);
      }
    } else {
      this.data[hash] = [key];
    }
  }

  remove(key) {
    const hash = this._hash(key);
    const loc = this.data[hash];

    if (loc) {
      let idx = this.data[hash].indexOf(key);
      if (idx > -1) {
        this.data[hash].splice(idx, 1);
      }
    }
  }

  contains(key) {
    const hash = this._hash(key);

    if (this.data[hash]) {
      return this.data[hash].includes(key);
    }

    return false;
  }
}

module.exports = MyHashSet;
