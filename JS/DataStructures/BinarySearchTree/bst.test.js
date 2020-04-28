const BST = require('./bst');

describe('Testing BST insert', () => {

  test('Testing insert 1', () => {
    const bst = new BST();
    bst.insert2(10);

    expect(bst.root.value).toBe(10);
    expect(bst.root.right).toBeNull();
    expect(bst.root.left).toBeNull();
  });

  test('Testing insert 1', () => {
    const bst = new BST();
    bst.insert2(10);
    bst.insert2(12);

    expect(bst.root.value).toBe(10);
    expect(bst.root.right.value).toBe(12);
    expect(bst.root.left).toBeNull();
  });

  test('Testing insert 1', () => {
    const bst = new BST();
    bst.insert2(10);
    bst.insert2(9);

    expect(bst.root.value).toBe(10);
    expect(bst.root.left.value).toBe(9);
    expect(bst.root.right).toBeNull();
  });

  test('Testing insert 1', () => {
    const bst = new BST();
    bst.insert2(10);
    bst.insert2(9);
    bst.insert2(11);
    bst.insert2(8)

    expect(bst.root.value).toBe(10);
    expect(bst.root.left.value).toBe(9);
    expect(bst.root.right.value).toBe(11);
    expect(bst.root.left.left.value).toBe(8);
    expect(bst.root.left.right).toBeNull();
  });

})