function canConstruct(ransomNote, magazine) {
  if (ransomNote.length > magazine.length) {
    return false;
  }
  const magazineFreq = frequencies(magazine);

  for (let c of ransomNote) {
    if (!magazineFreq[c] || magazineFreq[c] <= 0) {
      return false;
    }

    magazineFreq[c] = magazineFreq[c] - 1;
  }

  return true;
}

function frequencies(str) {
  const obj = {};
  for (let c of str) {
    obj[c] = obj[c] ? obj[c] + 1 : 1;
  }

  return obj;
}

main();

function main() {
  console.log(canConstruct('a', 'b'))
}
