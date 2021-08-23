// Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

// You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
//

function findRestaurant(arr1, arr2) {
  let obj = {};

  let res = [];
  let min = null;

  for (let [i, s] of arr1.entries()) {
    obj[s] = i;
  }

  for (let [i, s] of arr2.entries()) {
    if (obj[s] !== undefined) {
      if (min === null) {
        min = obj[s] + i;
        res = [s];
      } else if (obj[s] + i < min) {
        res = [s];
        min = obj[s] + i;
      } else if (obj[s] + i === min) {
        res.push(s);
      }
    }
  }

  return res;
}

