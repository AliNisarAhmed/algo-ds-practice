function twoSum(arr, target) {
	let obj = {};

	for (let i = 0; i < arr.length; i++) {
		if (obj[target - arr[i]] !== undefined) {
			return [i, obj[target - arr[i]]];
		} else {
			obj[arr[i]] = i;
		}
	}
}

console.log(twoSum([2, 7, 11, 15], 9));
