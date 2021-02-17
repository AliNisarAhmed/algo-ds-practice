function isFirstComeFirstServed(takeOut, dineIn, served) {
	let ti = 0, di = 0, currentOrder = 0;

	if (takeOut.length + dineIn.length !== served.length) {
		return false;
	}

	while (ti < takeOut.length || di < dineIn.length) {
		if (di === dineIn.length || served[currentOrder] === takeOut[ti]) {
			ti++;
			currentOrder++;
		}

		else if (ti === takeOut.length || served[currentOrder] === dineIn[di]) {
			di++;
			currentOrder++;
		}

		else {
			return false;
		}
	}

	return true;

}