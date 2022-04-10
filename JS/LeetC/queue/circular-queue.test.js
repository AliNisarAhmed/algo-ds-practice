const MyCircularQueue = require("./circular-queue.js");
let q;

beforeEach(() => {
  q = new MyCircularQueue();
});

describe("Test isFull and isEmpty", () => {
  test("New queue is empty", () => {
    expect(q.isEmpty()).toBeTruthy();
  });

  test('Enqueue items to fill up a queue to its limit', () => {
    q.enQueue(5);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    q.enQueue(4);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    q.enQueue(3);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    q.enQueue(2);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    q.enQueue(1);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeTruthy();

    expect(q.deQueue()).toEqual(true);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    expect(q.deQueue()).toEqual(true);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    expect(q.deQueue()).toEqual(true);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    expect(q.deQueue()).toEqual(true);
    expect(q.isEmpty()).toBeFalsy();
    expect(q.isFull()).toBeFalsy();

    expect(q.deQueue()).toEqual(true);
    expect(q.isEmpty()).toBeTruthy();
    expect(q.isFull()).toBeFalsy();

    expect(q.deQueue()).toEqual(false);
    expect(q.isEmpty()).toBeTruthy();
    expect(q.isFull()).toBeFalsy();
  })
});
