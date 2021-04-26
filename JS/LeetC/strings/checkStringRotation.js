// String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
// of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
// call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

function checkRotation(s1, s2) {
	let arr = [...s2];
	arr.push(...arr);

	return arr.join('').includes(s1);
}

console.log(checkRotation('waterbottle', 'erbottlewat'));
