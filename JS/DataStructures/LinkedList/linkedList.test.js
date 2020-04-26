const SinglyLinkedList = require('./linkedList');

describe('test Linked List: get', () => {

  let list;
  beforeEach(() => {
    list = new SinglyLinkedList();
    list.push(1).push(2).push(3).push(4);
  });

  test('gets the first element', () => {
    let result = [];
    for (let i = 0; i < list.length; i++) {
      result.push(list.get(i).value);
    }

    expect(result).toEqual([1, 2, 3, 4]);
  })
})

describe('Testing Linked List set', () => {

  let list;
  let oneItem;
  let empty;


  beforeEach(() => {
    list = new SinglyLinkedList()
    list.push(1).push(2).push(3).push(4);

    oneItem = new SinglyLinkedList();
    oneItem.push(1);

    empty = new SinglyLinkedList();
  });

  test('should set an item', () => {
    var index = 0;
    var value = 100;

    var result = list.set(value, index);
    var newItem = list.get(index);
    expect(result).toBeTruthy();
    expect(newItem.value).toBe(value);
  });
  test('should set an item', () => {
    var index = 1;
    var value = 100;

    var result = list.set(value, index);
    var newItem = list.get(index);
    expect(result).toBeTruthy();
    expect(newItem.value).toBe(value);
  });
  test('should set an item', () => {
    var index = 2;
    var value = 100;

    var result = list.set(value, index);
    var newItem = list.get(index);
    expect(result).toBeTruthy();
    expect(newItem.value).toBe(value);
  });
  test('should set an item', () => {
    var index = 3;
    var value = 100;

    var result = list.set(value, index);
    var newItem = list.get(index);
    expect(result).toBeTruthy();
    expect(newItem.value).toBe(value);
  });
  test('should set an item', () => {
    var index = 4;
    var value = 100;

    var result = list.set(value, index);
    var newItem = list.get(index);
    expect(result).toBeFalsy();
    expect(newItem).toBe(null);
  });

  test('should replace one item', () => {
    var index = 0;
    var value = 100;

    var result = oneItem.set(value, index);
    var newItem = oneItem.get(index);
    expect(result).toBeTruthy();
    expect(newItem.value).toBe(value);
  })

  test('Does not do anything with empty list', () => {
    var index = 0;
    var value = 100;

    var result = empty.set(value, index);
    var newItem = empty.get(index);
    expect(result).toBeFalsy();
    expect(newItem).toBeNull();
  })
});

describe('Test Linked List insert', () => {

  let list;
  let listLength;
  let oneItemList;
  let emptyList;
  let value = 100;

  beforeEach(() => {
    list = new SinglyLinkedList();
    list.push(0).push(1).push(2).push(3);
    listLength = list.length;

    oneItemList = new SinglyLinkedList();
    oneItemList.push(1);
  })

  test('Inserts the item at the index', () => {
    let index = 3;
    let result = list.insert(value, index);
    let newNode = list.get(index);

    expect(result).toBeTruthy();
    expect(newNode.value).toBe(value);
    expect(list.length).toBe(listLength + 1);
  });

  test('Inserts the item at the end', () => {
    let index = 4;
    let result = list.insert(value, index);
    let newNode = list.get(index);

    expect(result).toBeTruthy();
    expect(newNode.value).toBe(value);
    expect(list.length).toBe(listLength + 1);
  });

  test('Inserts at the beginning', () => {
    let index = 0;
    let result = oneItemList.insert(value, index);
    let newNode = oneItemList.get(index);

    expect(result).toBeTruthy();
    expect(newNode.value).toBe(value);
    expect(oneItemList.length).toBe(2);
    expect(oneItemList.head.value).toBe(value);
  });
})

describe('Testing Linked List remove', () => {
  let list;
  beforeEach(() => {
    list = new SinglyLinkedList();
    list.push(0).push(1).push(2).push(3);
  });

  test('Removes the item at the index', () => {
    let index = 3;
    let prev = list.get(index - 1);
    let nextValue = list.get(index + 1);
    let result = list.remove(index);

    expect(result).toBeTruthy();
    if (nextValue) {
      expect(list.get(index).value).toBe(nextValue.value);
    } else {
      expect(list.get(index - 1).value).toBe(prev.value);
    }
  })
})

describe('Testing Linked List: reverse', () => {
  let list;
  beforeEach(() => {
    list = new SinglyLinkedList();
    list.push(0).push(1).push(2).push(3);
  })
  test('Reverse a list', () => {
    list.reverse();

    expect(list.head.value).toBe(3);
    expect(list.tail.value).toBe(0);
    expect(list.head.next.value).toBe(2);
    expect(list.head.next.next.value).toBe(1);
    expect(list.head.next.next.next.value).toBe(0);
    expect(list.tail.next).toBeNull();
  })
})