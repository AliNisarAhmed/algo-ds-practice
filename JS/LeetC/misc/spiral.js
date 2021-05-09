// Comments on Time and Space Complexity:

// Time Complexity: O(n ^ 2) since we must fill n^2 elements.

// Space complexity: O(1), we are generating an array of size n ^ 2, but the returned result does not count towards space complexity. Apart from the returned array, we are using constant space.

function spiral(n) {
	// generate the n by n matrix which will be filled by the loops below and returned at the end
	let result = Array.from({ length: n}, () => Array.from({ length: n}));

	// val will go from 1 to n * n
	let val = 1;

	let j = 0;
	let i = 0;

	let left = 0;
	let right = n;
	let top = 1;
	let bottom = n;

	// we move one complete circuit around the spiral in one outer while loop
	while (left <= right && top <= bottom) {

		// left to right
		while (j < right) {
			result[i][j] = val;
			val++;
			j++;
		}

		i++;
		j--; // adjusting, since j would have gone "one over" or "one under" in the final step of the while loop

		// top to bottom
		while (i < bottom) {
			result[i][j] = val;
			val++;
			i++;
		}

		j--;
		i--; // again, "adjusting" the looping variable to appropriate value

		// right to left
		while (j >= left) {
			result[i][j] = val;
			val++;
			j--;
		}

		i--;
		j++;  // adjust

		// bottom to top
		while (i >= top) {
			result[i][j] = val;
			val++;
			i--;
		}

		i++;
		j++;  // adjust

		left++;
		right--;
		top++;
		bottom--;
	}

	return result;
}

console.log(spiral(2));
console.log(spiral(3));
console.log(spiral(4));
console.log(spiral(5));