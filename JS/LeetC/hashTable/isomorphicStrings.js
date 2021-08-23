function isIsomorphic(str1, str2) {
  if (str1.length !== str2.length) return false;

  let t1 = transform(str1);
  let t2 = transform(str2);

  return arrayAreEqual(t1, t2);
}

function arrayAreEqual(a1, a2) {
  for (let i = 0; i < a1.length; i++) {
    if (a1[i] !== a2[i]) {
      return false;
    }
  }

  return true;
}

// for each char in str, replace it with its first occurrence index and return the array
function transform(s) {
  let res = Array.from({ length: s.length });

  let obj = {};

  for (let [i, c] of [...s].entries()) {
    if (obj[c] === undefined) {
      obj[c] = i;
    }      

    res[i] = obj[c];
  }

  return res;
}



// ------ Solution two, using two hashmaps

function isIsomorphic(str1, str2) {
  // order of characters in two strings is preserved : e.g. title & paper
  //

  if (str1.length !== str2.length) return false;

  let obj1 = {};
  let obj2 = {};

  for (let i = 0; i < str1.length; i++) {
    let c1 = str1[i];
    let c2 = str2[i];

    if (obj1[c1] !== undefined) {
      if (obj1[c1] !== c2) {
        return false;
      }
    } else {
      obj1[c1] = c2;
    }

    if (obj2[c2] !== undefined) {
      if (obj2[c2] !== c1) {
        return false;
      }
    } else {
      obj2[c2] = c1;
    }
  }

  return true;
}
