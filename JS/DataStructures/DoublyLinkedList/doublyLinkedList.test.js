const DoublyLinkedList = require('./doublyLinkedList');

describe('Testing pop', () => {
	let list;
	let values;
	let len;

	beforeEach(() => {
		list = new DoublyLinkedList();
		values = [1, 2, 3, 4, 5];
		len = values.length;
		values.forEach((v) => list.push(v));
	});

	test('removes the last elements', () => {
		for (let i = len - 1; i >= 0; i--) {
			let removed = list.pop();
			expect(removed.prev).toBeNull();
			expect(removed.value).toBe(values[i]);
			expect(list.length).toBe(i);
		}

		expect(list.pop()).toBeNull();
	});
});

describe('Testing shift', () => {
	let list;
	let values;
	let len;

	beforeEach(() => {
		list = new DoublyLinkedList();
		values = [1, 2, 3, 4, 5];
		len = values.length;
		values.forEach((v) => list.push(v));
	});

	test('removes the last elements', () => {
		for (let i = 0; i < len; i++) {
			let removed = list.shift();
			expect(removed.next).toBeNull();
			expect(removed.value).toBe(values[i]);
			expect(list.length).toBe(len - i - 1);
		}

		expect(list.pop()).toBeNull();
	});
});

describe('Testing unshift', () => {
	test('should add elements to the beginning', () => {
		let list = new DoublyLinkedList();
		list.unshift(5);
		expect(list.length).toBe(1);
		expect(list.head.value === list.tail.value).toBeTruthy();

		list.unshift(4);
		expect(list.length).toBe(2);
		expect(list.head.value).toBe(4);
		expect(list.head.prev).toBeNull();
		expect(list.head.next.value).toBe(5);
		expect(list.tail.value).toBe(5);
		expect(list.tail.next).toBeNull();
	});
});

describe('Testing get', () => {
	let list;
	let values;
	let len;

	beforeEach(() => {
		list = new DoublyLinkedList();
		values = [1, 2, 3, 4, 5];
		len = values.length;
		values.forEach((v) => list.push(v));
	});

	test('should get the element at the index', () => {
		for (let i = 0; i < len; i++) {
			let elem = list.get(i);
			expect(elem.value).toBe(values[i]);
		}
	});
});

describe('Testing insert', () => {
	let list;
	let values;
	let len;

	beforeEach(() => {
		list = new DoublyLinkedList();
		values = [1, 2, 3, 4, 5];
		len = values.length;
		values.forEach((v) => list.push(v));
	});

	test('testing insert', () => {
		list.insert(0, 100);
		expect(list.get(0).value).toBe(100);
		expect(list.length).toBe(6);
	});
	test('testing insert 2', () => {
		list.insert(3, 300);
		expect(list.get(3).value).toBe(300);
		expect(list.get(4).value).toBe(4);
	});
	test('testing insert 3', () => {
		list.insert(5, 500);
		expect(list.get(5).value).toBe(500);
		expect(list.get(6)).toBeNull();
	});
});

describe('Testing remove', () => {
	let list;
	let values;
	let len;

	beforeEach(() => {
		list = new DoublyLinkedList();
		values = [1, 2, 3, 4, 5];
		len = values.length;
		values.forEach((v) => list.push(v));
	});

	test('Testing remove 1', () => {
		list.remove(0);
		expect(list.get(0).value).toBe(2);
		expect(list.length === 4).toBeTruthy();
	});
	test('Testing remove 2', () => {
		list.remove(2);
		expect(list.get(2).value).toBe(4);
		expect(list.length === 4).toBeTruthy();
	});
	test('Testing remove 4', () => {
		list.remove(0);
		expect(list.get(4)).toBeNull();
		expect(list.length === 4).toBeTruthy();
	});


});
