function isAnagra(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }
  const obj: Record<string, number> = {};  
  
  for (let c of s) {
    obj[c] = obj[c] ? obj[c] + 1 : 1;
  }

  for (let c of t) {
    if (!obj[c]) {
      return false;
    } else {
      obj[c] -= 1;
    }
  }
 
  return true;
};


export default isAnagram;
