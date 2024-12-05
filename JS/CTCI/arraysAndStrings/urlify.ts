function urlify(str: string) {
  const arr = str.trim().split(/\s+/g).filter(Boolean);
  return arr.join("%20");
}

console.log(urlify("Mr John Smith    "), ".");
