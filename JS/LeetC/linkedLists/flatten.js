// You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

// Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

const Stack = require('../stack/stack.js');


function flatten(head) {
  if (!head) return head;

  let stack = new Stack();

  stack.push(head);

  let prev;

  while(!stack.isEmpty()) {
    let current = stack.pop();
    current.prev = prev;

    if (prev) {
      prev.next = current;
    }

    if (current.next) {
      stack.push(current.next);
    }

    if (current.child) {
      stack.push(current.child);
      current.child = null;
    }
  }

  return head;
}

function flatten(head) {
	if (!head) return head;

	let children = flatten(head.child);
	let rest = flatten(head.next);

	if (children) {
		head.next = children;
		children.prev = head;
		head.child = null

		let last = children;

		while (last.next) {
			last = last.next;
		}

		last.next = rest;

		if (rest) {
			rest.prev = last;
		}

	} else if (rest) {
		head.next = rest;
		rest.prev = head;
	}

	return head;
}

let l1 = {
	val: 1,
	next: {
		val: 4,
		prev: null,
		next: null,
		child: null,
	},
	prev: null,
	child: {
		val: 2,
		next: {},
		prev: null,
		child: {
			val: 3,
			next: null,
			prev: null,
			child: null,
		},
	},
};

console.log(flatten(l1));
