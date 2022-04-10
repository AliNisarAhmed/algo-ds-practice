const combinationSum = require('./combinationSum.js')

describe('test combination sum', () => {

  test('Test empty list', () => {
    const res = combinationSum([], 10);
    expect(res).toEqual([]);
  })

})
