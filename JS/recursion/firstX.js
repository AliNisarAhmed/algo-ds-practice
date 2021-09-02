function firstX(str, i = 0) {
  if (str[i] === 'x') {
    return i;
  }

  return firstX(str, i + 1);

}

console.log(firstX('abcx123'))

