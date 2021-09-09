// dict :: string[]
//
// 
// Returns true if either of the following conditions are met (otherwise returns false):

//     There is no word in dictionary whose abbreviation is equal to word's abbreviation.
//     For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.

class ValidWordAbbr {
  constructor(dict) {
    this.dict = this.generateDict(dict);
  }

  isUnique(word) {
    let ab = this.abbrev(word);
    if (!this.dict[ab]) {
      return true;
    }

    return this.dict[ab].every(w => w === word);
  }

  abbrev(word) {
    if (word.length <= 2) return word;
    return `${word[0]}${word.length - 2}${word[word.length - 1]}`;
  }

  generateDict(words) {
    let res = {};

    for (let word of words) {
      let ab = this.abbrev(word);

      if (res[ab]) {
        res[ab].push(word);
      } else {
        res[ab] = [word];
      }
    }
    return res;
  }

}
