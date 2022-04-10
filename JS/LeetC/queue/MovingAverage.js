
class MovingAverage {
  constructor(k) {
    this.size = k;
    this.count = 0;
    this.sum = 0;
    this.data = Array.from({ length: k }, () => 0)
  }

  next(v) {
    this.count++;

    this.data.unshift(v);

    let last = 0;

    if (this.data.length > this.size) {
      last = this.data.pop()
    }

    this.sum = this.sum + v - last;

    return this.sum / (Math.min(this.size, this.count))

  }
}
