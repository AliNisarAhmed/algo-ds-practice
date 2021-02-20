function maxProfit(arr) {
	// the idea is to "collect" each increment as we go along the arr

	let profit = 0;

	for (let i = 1; i < arr.length; i++) {
		if (arr[i] > arr[i - 1]) {
			profit += arr[i] - arr[i - 1];
		}
	}

	return profit;
}

function maxProfit(arr) {
	let buy = arr[0];
	let sell = arr[0];

	let profit = 0;

	let i = 0;

	while (i < arr.length - 1) {

		while (i < arr.length - 1 && arr[i] >= arr[i + 1]) {
			i++;
		}

		buy = arr[i];

		while (i < arr.length - 1 && arr[i] <= arr[i + 1]) {
			i++;
		}

		sell = arr[i];

		profit += buy - sell;

	}

	return profit;
}


// My Solution:

function maxProfit(arr) {
	let profit = 0;
	let subProfit = 0;
	let low = arr[0];
	let hi = null;

	for (let i = 1; i < arr.length; i++) {
		let current = arr[i];
		if (low === null) {
			low = current;
		}

		else {
			if (current < low) {
				if (hi === null) {
					low = current;
				}

				else {
					profit += subProfit;
					subProfit = 0;
					low = current;
					hi = null;
				}
			}

			else if (current >= low) {

				if (hi === null) {
					hi = current;
					subProfit = hi - low;

					if (i === arr.length - 1) {
						profit += subProfit;
						subProfit = 0;
					}

				}

				else {

					if (current > hi) {
						hi = current;
						subProfit = hi - low;

						if (i === arr.length - 1) {
							profit += subProfit;
							subProfit = 0;
						}
					}

					else if (current < hi) {
						profit += subProfit;
						subProfit = 0;
						low = current;
						hi = null;
					}
				}
			}
		}
	}

	return profit + subProfit;
}

console.log(maxProfit([1,2,4,2,5,7,2,4,9,0]));