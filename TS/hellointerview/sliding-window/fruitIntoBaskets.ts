
function fruitToBaskets(fruits: number[]): number {
  let start = 0;
  let maxFruit = 0;
  let basket: { [key: number]: number } = {};

  for (let end = 0; end < fruits.length - 1; end++) {
    basket[fruits[end]] = (basket[fruits[end]] || 0) + 1;

    while (Object.keys(basket).length > 2) {
      // invalid basket, start deleting from start
      basket[fruits[start]]--;
      if (basket[fruits[start]] === 0) {
        delete basket[fruits[start]];
      }
      start++;
    }

    maxFruit = Math.max(maxFruit, end - start + 1);
  }

  return maxFruit;
}
