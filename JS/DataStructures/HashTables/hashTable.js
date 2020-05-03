function hash(key, arrayLen) {
  let total = 0;
  let WEIRD_PRIME = 83;
  for (let i = 0; i < Math.min(key.length, 100); i++) {
    let char = key[i];
    let value = char.charCodeAt(0) - 96;
    total = (total * WEIRD_PRIME + value) % arrayLen;
  }
  return total;
}

class HashTable {
  constructor( size = 53) {
    this.keyMap = new Array(size);
  }

  _hash(key) {
    let total = 0;
    let WEIRD_PRIME = 83;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i];
      let value = char.charCodeAt(0) - 96;
      total = (total * WEIRD_PRIME + value) % this.keyMap.length;
    }
    return total;
  }

  set(key, value) {
    let hash = this._hash(key);
    if (this.keyMap[hash]) {
      let index = this.keyMap[hash].findIndex(([k, v]) => k === key);
      if (index === -1) {
        this.keyMap.push([key, value]);
      } else {
        this.keyMap[hash][index][1] = value;
      }
    } else {
      this.keyMap[hash] = [ [key, value] ];
    }
  }

  get(key) {
    const hash = this._hash(key);
    let found = this.keyMap[hash].find(([k, v]) => k === key);

    if (found) {
      return found[1];
    }

    return null;
  }

  keys() {
    const keys = [];
    for (let i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (let j = 0; j < this.keyMap[i].length; j++) {
          if (!keys.includes(this.keyMap[i][j][0])) {
            keys.push(this.keyMap[i][j][0]);
          }
        }
      }
    }

    return keys;
  }

  values() {
    const values = [];
    for (let i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for (let j = 0; j < this.keyMap[i].length; j++) {
          if (!values.includes(this.keyMap[i][j][1])) {
            values.push(this.keyMap[i][j][1]);
          }
        }
      }
    }

    return values;
  }
}