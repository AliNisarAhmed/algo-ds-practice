// https://www.youtube.com/watch?v=fMSJSS7eO1w&feature=emb_logo

function rotate(matrix) {
	let left = 0; r = matrix.length - 1;

	while (left < right) {
		for (let i = 0; i < right - left; i++) {
			let top = left;
			let bottom = right;

			topLeft = matrix[top][left + i];
			matrix[top][left + i] = matrix[bottom- i][left]
			matrix[bottom - i][left] = matrix[bottom][right - i]
			matrix[bottom][right - i] = matrix[top + i][right]
			matrix[top + i][right] = topLeft;
		}

		right--;
		left--;
	}
}



function rotate(matrix) {
	let n = matrix[0].length;
	let first = Math.floor(n / 2);
	let second = n % 2;
	for (let i = 0; i < (first + second); i++) {
		for (let j = 0; j < first; j++) {
			let temp = matrix[n - 1 - j][i];
			matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
			matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
			matrix[j][n - 1 - i] = matrix[i][j]
			matrix[i][j] = temp;
		}
	}
}

function rotate(matrix) {
	transpose(matrix);

	for (let row of matrix) {
		row.reverse();
	}
}

function transpose(matrix) {
	for (let i = 0; i < matrix.length; i++) {
		for (let j = i; j < matrix.length; j++) {
			[matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
		}
	}
}

const m1 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
];

const m2 = [
	[5, 1, 9, 11],
	[2, 4, 8, 10],
	[13, 3, 6, 7],
	[15, 14, 12, 16],
];

rotate(m1);
// transpose(m2);

console.log(m1);
console.log(m2);
