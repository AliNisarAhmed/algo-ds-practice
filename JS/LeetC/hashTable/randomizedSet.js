class RandomizedSet {
  constructor() {
    this.dict = {};
    this.index = [];
  }

  insert(val) {
    if (this.dict[val] !== undefined) {
      return false;
    }

    this.dict[val] = this.index.length;
    this.index.push(val);

    return true;
  }

  remove(val) {
    if (this.dict[val] !== undefined) {
      let index = this.dict[val];
      this.dict[val] = undefined;

      let lastElement = this.index.pop();
      if (this.index.length === index) return true;

      this.index[index] = lastElement;
      this.dict[lastElement] = index;
      return true;
    }

    return false;
  }

  getRandom() {
    let randomInt = this.getRandomBetween(0, this.index.length - 1);
    return this.index[randomInt];
  }

  getRandomBetween(min, max) {
    return Math.floor(Math.random() * (max + 1 - min)) + min;
  }
}
