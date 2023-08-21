function openLock(deadends, target) {
  let queue = [];
  debugger;
  queue.unshift(["0000", 0]);
  const seen = new Set(deadends);
  console.log(seen);

  while (queue.length > 0) {
    let [node, depth] = queue.pop();
    if (node === target) {
      return depth;
    }

    if (seen.has(node)) {
      continue;
    }

    seen.add(node);

    for (let nei of neighbors(node)) {
      console.log({ nei, depth });
      queue.unshift([nei, depth + 1]);
    }
  }

  return -1;
}

function* neighbors(node) {
  for (let i of [0, 1, 2, 3]) {
    let x = Number(node[i]);

    for (let d of [1, -1]) {
      y = mod(x + d, 10);
      yield node.slice(0, i) + String(y) + node.slice(i + 1);
    }
  }
}

function mod(n, m) {
  return ((n % m) + m) % m;
}

(() => {
  openLock(["0201", "0101", "0102", "1212", "2002"], "0202");
})();
