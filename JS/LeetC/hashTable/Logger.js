class Logger {
  constructor() {
    this.state = {};
  }

  shouldPrintMessage(timestamp, message) {
    let lastCall = this.state[message];

    if (lastCall !== undefined) {
      if (timestamp < lastCall + 10) {
        return false;
      }
    }

    this.state[message] = timestamp;
    return true;
  }
}
