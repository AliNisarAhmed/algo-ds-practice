function merge(nums1, m, nums2, n) {

	let i = m - 1;
	let j = n - 1;

	for (let k = m + n - 1; k >= 0; k--) {
		if (j < 0) {
			nums1[k] = nums1[i];
			i--
		} else if (i < 0) {
			nums1[k] = nums2[j];
			j--;
		} else if (nums1[i] < nums2[j]) {
			nums1[k] = nums2[j];
			j--;
		} else {
			nums1[k] = nums1[i];
			i--;
		}
	}
}

let arr1 = [4,5,6,0,0,0]
let arr2 = [1,2,3]

console.log(merge(arr1, 3, arr2, 3))