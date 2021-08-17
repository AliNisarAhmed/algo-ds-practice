

class MyHashMap {
  constructor() {
    this.keySize = 2069;
    this.data = Array.from({ length: this.keySize });
  }

  _hash(x) {
    return x % this.keySize;
  }

  put(key, value) {
    const hash = this._hash(key);

    if (this.data[hash]) {

      const entryIndex = this.data[hash].findIndex(v => v && v[0] === key);

      if (entryIndex > -1) {
        this.data[hash][entryIndex][1] = value;
      } else {
        this.data[hash].push([key, value]);
      }

    } else {
      this.data[hash] = [ [key, value] ];
    }
  }

  get(key) {
    const hash = this._hash(key);

    if (this.data[hash]) {
      const entry = this.data[hash].find(v => v && v[0] === key);

      if (entry) {
        return entry[1];
      }
    }

    return -1;
  }

  remove(key) {
    const hash = this._hash(key);

    if (this.data[hash]) {
      let idx = this.data[hash].findIndex(v => v && v[0] === key);

      if (idx > -1) {
        this.data[hash].splice(idx, 1);
      }
    }
  }
}
