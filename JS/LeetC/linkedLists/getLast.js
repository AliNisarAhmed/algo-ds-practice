
function getLast(node) {
  if (!node) return null;

  let current = node;

  while (current.next) {
    current = current.next;
  }

  return current;
}

let l1 = {
  val: 1, 
  next: { 
    val: 2, 
    next: null
  }
}

console.log(getLast(l1))
