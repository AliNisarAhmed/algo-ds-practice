function merge(nums1, m, nums2, n) {
	let left = m - 1;
	let right = n - 1;

	for (let k = m + n - 1; k >= 0; k--) {

		// another way
		// if (right < 0) {
		// 	break;
		// }

		// if (left >= 0 && nums1[left] > nums2[right]) {
		// 	nums1[k] = nums1[left];
		// 	left--;
		// } else {
		// 	nums1[k] = nums2[right];
		// 	right--;
		// }

		if (left < 0) {
			nums1[k] = nums2[right];
			right--;
		} else if (right < 0) {
			nums1[k] = nums1[left];
			left--;
		} else if (nums1[left] >= nums2[right]) {
			nums1[k] = nums1[left];
			left--;
		} else if (nums1[left] < nums2[right]) {
			nums1[k] = nums2[right];
			right--;
		}
	}
}

let nums1 = [1, 2, 3, 0, 0, 0];
let nums2 = [2, 5, 6];

merge(nums1, 3, nums2, 3);

// function merge(nums1, m, nums2, n) {

// 	let i = m - 1;
// 	let j = n - 1;

// 	for (let k = m + n - 1; k >= 0; k--) {
// 		if (j < 0) {
// 			nums1[k] = nums1[i];
// 			i--
// 		} else if (i < 0) {
// 			nums1[k] = nums2[j];
// 			j--;
// 		} else if (nums1[i] < nums2[j]) {
// 			nums1[k] = nums2[j];
// 			j--;
// 		} else {
// 			nums1[k] = nums1[i];
// 			i--;
// 		}
// 	}
// }
