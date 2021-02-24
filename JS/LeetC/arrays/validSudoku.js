function isValidSudoku(board) {
	const areRowsValid = checkBoardValidity(board)

	if (!areRowsValid) return false;

	const cols = getColumns(board);

	const areColsValid = checkBoardValidity(cols);

	if (!areColsValid) return false;

	const boxes = getBoxes(board);

	const areBoxesValid = checkBoardValidity(boxes);

	if (!areBoxesValid) return false;

	return true;

}

function getBoxes(board) {
	let result = [];

	for (let i = 0; i < board.length; i++) {
		for (let j = 0; j < board.length; j++) {
			let boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
			if (!result[boxIndex]) {
				result[boxIndex] = [];
			}
			result[boxIndex].push(board[i][j])
		}
	}

	return result;
}

function checkBoardValidity(board) {
	return board
		.map((row) => hasDuplicate(row.filter((r) => r !== '.')))
		.every((res) => res === true);
}

function getColumns(board) {
	let result = [];
	for (let i = 0; i < board.length; i++) {
		result[i] = [];
		for (let j = 0; j < board.length; j++) {
			result[i].push(board[j][i]);
		}
	}

	return result;
}

function hasDuplicate(arr) {
	const obj = {};

	for (let elem of arr) {
		if (obj[elem]) {
			return false;
		} else {
			obj[elem] = true;
		}
	}

	return true;
}

// -------------------

let board1 = [
	['5', '3', '.', '.', '7', '.', '.', '.', '.'],
	['6', '.', '.', '1', '9', '5', '.', '.', '.'],
	['.', '9', '8', '.', '.', '.', '.', '6', '.'],
	['8', '.', '.', '.', '6', '.', '.', '.', '3'],
	['4', '.', '.', '8', '.', '3', '.', '.', '1'],
	['7', '.', '.', '.', '2', '.', '.', '.', '6'],
	['.', '6', '.', '.', '.', '.', '2', '8', '.'],
	['.', '.', '.', '4', '1', '9', '.', '.', '5'],
	['.', '.', '.', '.', '8', '.', '.', '7', '9'],
];

console.log(isValidSudoku(board1));
