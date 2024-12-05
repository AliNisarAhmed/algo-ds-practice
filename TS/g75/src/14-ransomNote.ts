function canConstruct(ransomNote: string, magazine: string) {
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

function frequencies(str: string) {
  const obj: Record<string, number> = {};
  for (let c of str) {
    obj[c] = obj[c] ? obj[c] + 1 : 1;
  }

  return obj;
}
